from decimal import Decimal

from django.core.management.base import BaseCommand
from lessonapp.models import Product


class Command(BaseCommand):
    help = "Create product."

    def add_arguments(self, parser):
        parser.add_argument('name_product', type=str, help='product name')

    def handle(self, *args, **kwargs):
        name_product = kwargs.get('name_product')

        product = Product(
            name_product=name_product,
            description_product='This is a sample product',
            price_product=Decimal('19.99'),
            number_product=100,
        )
        product.save()
        self.stdout.write(f'Created product: {product.name_product}')
