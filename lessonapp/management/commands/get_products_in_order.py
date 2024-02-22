from django.core.management.base import BaseCommand
from lessonapp.models import Order


class Command(BaseCommand):
    help = "Get all orders by user id."

    def add_arguments(self, parser):
        parser.add_argument('pk_order', type=int, help='Order ID')

    def handle(self, *args, **kwargs):
        pk_order = kwargs.get('pk_order')
        order = Order.objects.filter(pk=pk_order).first()

        if order is not None:
            products = order.products.all()
            intro = f'All products of order №{pk_order}\n'
            text = '\n'.join(f'Name: {product.name_product}; '
                             f'Price: {str(product.price_product)}; '
                             f'Product Quantity: {str(product.number_product)}'
                             for product in products)
            self.stdout.write(f'{intro}{text}')
