from django.core.management.base import BaseCommand
from lessonapp.models import Order, Product, User


class Command(BaseCommand):
    help = "Create order."

    def add_arguments(self, parser):
        parser.add_argument('pk_user', type=int, help='User ID')
        parser.add_argument('pks_products', nargs='+', type=int, help='Product ID')

    def handle(self, *args, **kwargs):
        pk_user = kwargs.get('pk_user')
        pks_products = kwargs.get('pks_products')

        product_prices = Product.objects.filter(pk__in=pks_products).values_list('price_product', flat=True)
        total_sum = sum(product_prices)
        customer = User.objects.filter(pk=pk_user).first()

        order = Order(
            customer=customer,
            general_sum=total_sum,
        )

        order.save()
        order.products.set(pks_products)

        self.stdout.write(f'Created order #{order.pk} for {customer.name}')
