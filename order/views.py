from django.db import transaction, OperationalError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from cart.models import Cart
from cart_items.models import CartItem
from order_items.models import OrderItem
from products.models import Product
from .models import Order
from .permissions import IsOrderAccess
from .serializers import OrderSerializer
from rest_framework import status


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsOrderAccess]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'CUSTOMER':
            return Order.objects.filter(user=user)
        if user.role == 'STORE_OWNER':
            return Order.objects.filter(items__product__store__owner=user).distinct()
        return Order.objects.none()

    def perform_create(self, serializer):
        user = self.request.user

        cart = Cart.objects.filter(user=user).first()
        if not cart:
            raise ValidationError('Cart not found')

        # ✅ FIX 1: Get cart item IDs before the transaction
        # We only read IDs here (safe), actual product data is read INSIDE the transaction
        cart_item_ids = list(
            CartItem.objects.filter(cart=cart).values_list('id', flat=True)
        )
        if not cart_item_ids:
            raise ValidationError('Cart is empty')

        try:
            with transaction.atomic():
                order = serializer.save(user=user)
                order_items = []

                # ✅ FIX 2: Read cart items INSIDE the transaction
                cart_items = CartItem.objects.select_related(
                    'product', 'product__store'
                ).filter(id__in=cart_item_ids)

                for item in cart_items:
                    # ✅ FIX 3: select_for_update(nowait=True)
                    # Lock this specific product row
                    # nowait=True → if already locked, raise error immediately
                    # instead of waiting forever
                    product = Product.objects.select_for_update(
                        nowait=True
                    ).get(id=item.product_id)

                    # ✅ Stock check happens AFTER we have the lock
                    # so the stock value is guaranteed to be fresh and accurate
                    if item.quantity > product.stock:
                        raise ValidationError(
                            f'Not enough stock for {product.name}. '
                            f'Available: {product.stock}, Requested: {item.quantity}'
                        )

                    product.stock -= item.quantity
                    product.save()

                    order_items.append(OrderItem(
                        order=order,
                        product=product,
                        quantity=item.quantity,
                        price=product.price
                    ))

                OrderItem.objects.bulk_create(order_items)
                CartItem.objects.filter(cart=cart).delete()

        # ✅ FIX 4: Handle the case where a product is already locked
        # by another concurrent request
        except OperationalError:
            raise ValidationError(
                'Another request is processing this product. '
                'Please try again in a moment.'
            )

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()

        if order.status == 'CANCELLED':
            raise ValidationError('Order already cancelled')

        try:
            with transaction.atomic():
                order_items = OrderItem.objects.select_related(
                    'product'
                ).filter(order=order)

                for item in order_items:
                    # ✅ Same fix applied to cancel as well
                    product = Product.objects.select_for_update(
                        nowait=True
                    ).get(id=item.product.id)

                    product.stock += item.quantity
                    product.save()

                order.status = 'CANCELLED'
                order.save()

        except OperationalError:
            raise ValidationError(
                'Cannot cancel right now, a transaction is in progress. '
                'Please try again.'
            )

        return Response(
            {'message': 'Order cancelled successfully'},
            status=status.HTTP_200_OK
        )