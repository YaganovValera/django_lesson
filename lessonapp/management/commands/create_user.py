from django.core.management.base import BaseCommand
from lessonapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def add_arguments(self, parser):
        parser.add_argument('email', type=str, help='User email')
        parser.add_argument('phone', type=str, help='User phone')

    def handle(self, *args, **kwargs):
        email = kwargs.get('email')
        phone = kwargs.get('phone')

        user = User(
            name='John Doe',
            email=email,
            phone=phone,
            address='123 Main St',
        )
        user.save()
        self.stdout.write(f'Created client: {user.name}')
