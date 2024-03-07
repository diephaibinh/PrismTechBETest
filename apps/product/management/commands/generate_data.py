from django.core.management.base import BaseCommand

from apps.product.services.generate_data_services import generate_data


class Command(BaseCommand):
    def handle(self, *args, **options):
        generate_data()