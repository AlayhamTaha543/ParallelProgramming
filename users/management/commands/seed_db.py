from decimal import Decimal

from django.core.management.base import BaseCommand
from django.db import transaction

from cart.models import Cart
from cart_items.models import CartItem
from order.models import Order
from order_items.models import OrderItem
from payments.models import Payment
from products.models import Product
from store.models import Store
from users.models import User


class Command(BaseCommand):
    help = 'Seed the database with sample data for all project tables.'

    @transaction.atomic
    def handle(self, *args, **options):
        owner = self.ensure_user(
            username='store_owner_1',
            email='owner1@example.com',
            password='Pass12345!',
            role=User.Roles.STORE_OWNER,
            first_name='Store',
            last_name='Owner',
        )

        customer = self.ensure_user(
            username='customer_1',
            email='customer1@example.com',
            password='Pass12345!',
            role=User.Roles.CUSTOMER,
            first_name='Sample',
            last_name='Customer',
        )

        customer_two = self.ensure_user(
            username='customer_2',
            email='customer2@example.com',
            password='Pass12345!',
            role=User.Roles.CUSTOMER,
            first_name='Second',
            last_name='Customer',
        )

        store = Store.objects.get_or_create(
            name='Demo Store',
            owner=owner,
            defaults={
                'description': 'Sample store used for development data.',
            },
        )[0]

        products = [
            self.ensure_product(
                store=store,
                name='Wireless Mouse',
                description='A quiet wireless mouse for everyday use.',
                price=Decimal('19.99'),
                stock=50,
            ),
            self.ensure_product(
                store=store,
                name='Mechanical Keyboard',
                description='A compact mechanical keyboard with tactile switches.',
                price=Decimal('79.99'),
                stock=25,
            ),
            self.ensure_product(
                store=store,
                name='USB-C Hub',
                description='A 6-in-1 USB-C hub for laptops and tablets.',
                price=Decimal('34.50'),
                stock=40,
            ),
        ]

        cart_one = self.ensure_cart(customer)
        cart_two = self.ensure_cart(customer_two)

        self.ensure_cart_item(cart_one, products[0], quantity=2)
        self.ensure_cart_item(cart_one, products[1], quantity=1)
        self.ensure_cart_item(cart_two, products[2], quantity=3)

        order_one = self.ensure_order(customer, store, Order.Status.PENDING)
        order_two = self.ensure_order(customer_two, store, Order.Status.PAID)

        self.ensure_order_item(order_one, products[0], quantity=2, price=products[0].price)
        self.ensure_order_item(order_one, products[1], quantity=1, price=products[1].price)
        self.ensure_order_item(order_two, products[2], quantity=3, price=products[2].price)

        self.ensure_payment(order_two, amount=products[2].price * 3, status=Payment.Status.COMPLETED)

        self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))

    def ensure_user(self, username, email, password, role, first_name='', last_name=''):
        user = User.objects.filter(username=username).first()
        if user:
            return user

        return User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role,
            first_name=first_name,
            last_name=last_name,
        )

    def ensure_product(self, store, name, description, price, stock):
        product, _ = Product.objects.get_or_create(
            store=store,
            name=name,
            defaults={
                'description': description,
                'price': price,
                'stock': stock,
            },
        )
        return product

    def ensure_cart(self, user):
        cart, _ = Cart.objects.get_or_create(user=user)
        return cart

    def ensure_cart_item(self, cart, product, quantity):
        cart_item, _ = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={
                'quantity': quantity,
            },
        )
        if cart_item.quantity != quantity:
            cart_item.quantity = quantity
            cart_item.save(update_fields=['quantity', 'total_price'])
        return cart_item

    def ensure_order(self, user, store, status):
        order, _ = Order.objects.get_or_create(
            user=user,
            store=store,
            status=status,
        )
        return order

    def ensure_order_item(self, order, product, quantity, price):
        order_item, _ = OrderItem.objects.get_or_create(
            order=order,
            product=product,
            defaults={
                'quantity': quantity,
                'price': price,
            },
        )
        if order_item.quantity != quantity or order_item.price != price:
            order_item.quantity = quantity
            order_item.price = price
            order_item.save(update_fields=['quantity', 'price'])
        return order_item

    def ensure_payment(self, order, amount, status):
        payment, _ = Payment.objects.get_or_create(
            order=order,
            defaults={
                'amount': amount,
                'status': status,
            },
        )
        if payment.amount != amount or payment.status != status:
            payment.amount = amount
            payment.status = status
            payment.save(update_fields=['amount', 'status'])
        return payment