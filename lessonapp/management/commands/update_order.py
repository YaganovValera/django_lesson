from django.core.management.base import BaseCommand
from lessonapp.models import Order, Product


class Command(BaseCommand):
    help = "Update order."

    def add_arguments(self, parser):
        parser.add_argument('pk_order', type=int, help='Order ID')
        parser.add_argument('pks_products', nargs='+', type=int, help='new Product ID')

    def handle(self, *args, **kwargs):
        pk_order = kwargs.get('pk_order')
        pks_products = kwargs.get('pks_products')

        order = Order.objects.filter(pk=pk_order).first()

        product_prices = Product.objects.filter(pk__in=pks_products).values_list('price_product', flat=True)
        total_sum = sum(product_prices)

        order.general_sum = total_sum
        order.save()
        order.products.set(pks_products)

        self.stdout.write(f'update order #{order.pk} for {order.general_sum}')
