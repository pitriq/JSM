from django.core.management.base import BaseCommand, CommandError

from accounts.models import User


class Command(BaseCommand):
    """
    Creates a mock superuser, only meant to be used during development.
    """
    help = 'Creates a superuser with email admin@admin.xdxd'

    def handle(self, *args, **options):
        admin = User.objects.filter(email='admin@admin.xdxd')
        if admin:
            raise CommandError('Mock admin user already exists!')
        User.objects.create_superuser(
            'admin@admin.xdxd', 'El', 'admin', 'adminadmin')
        self.stdout.write(self.style.SUCCESS(
            'Successfully created mock admin'))
