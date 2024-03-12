# delete_data.py

from django.core.management.base import BaseCommand

from directions.models import Place
# from .models import Place  # Import your model

class Command(BaseCommand):
    help = 'Delete all data from the BusLocation model'

    def handle(self, *args, **options):
        Place.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all data'))
