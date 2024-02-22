from django.core.management.base import BaseCommand
from lessonapp.models import Order, User


class Command(BaseCommand):
    help = "Get all orders by user id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()

        if user is not None:
            orders = Order.objects.filter(customer=user)
            intro = f'All orders of {user.name}\n'
            text = '\n'.join(f'Order № {order.id}; Check: {str(order.general_sum)}' for order in orders)
            self.stdout.write(f'{intro}{text}')

    