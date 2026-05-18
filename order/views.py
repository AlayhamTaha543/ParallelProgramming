from django.db import transaction

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action

from cart.models import Cart
from cart_items.models import CartItem
from order.tasks import send_order_email
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
        cart_items = list(
            CartItem.objects.select_related('product', 'product__store')
            .filter(cart=cart)
        )
        if not cart_items:
            raise ValidationError('Cart is empty')
        with transaction.atomic():
            order = serializer.save(user=user)
            order_items = []
            
            for item in cart_items:
                product = Product.objects.select_for_update().get(id=item.product_id)
                if item.quantity > product.stock:
                    raise ValidationError(f'Not enough stock for {product.name}')
                
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

        # Asyncronous sending an email in order using redis & celery
        transaction.on_commit(
            lambda: (
                send_order_email.delay(user.email, order.id)
            )
        )

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):

        order = self.get_object()

        if order.status == 'CANCELLED':
            raise ValidationError('Order already cancelled')

        with transaction.atomic():
            order_items = (
                OrderItem.objects
                .select_related('product')
                .filter(order=order)
            )

            for item in order_items:
                product = (
                    Product.objects
                    .select_for_update()
                    .get(id=item.product.id)
                )
                product.stock += item.quantity
                product.save()
            order.status = 'CANCELLED'
            order.save()

        return Response(
            {'message': 'Order cancelled successfully'},
            status=status.HTTP_200_OK
        )