# your_app/management/commands/feed_places.py

from django.core.management.base import BaseCommand
from directions.models import Place2

class Command(BaseCommand):
    help = 'Feed the Place2 table with valid lat ,lng and title values'

    def handle(self, *args, **options):
        places_data = [
            {'lat': 18.757574205947943, 'lng': 73.41131875561207, 'title':"Lonavala"},
            {'lat': 18.66859220261879, 'lng': 74.11946893730655, 'title':"Shikrapur"},
            {'lat': 18.47344637478693, 'lng':  74.55450534776311, 'title':"Daund"},
            {'lat': 18.189537078904564, 'lng': 74.58557937708143, 'title':"Baramati"},
            {'lat': 18.126793192301598, 'lng': 75.02061578753802, 'title':"Indapur"},
            {'lat': 17.894076052621582, 'lng': 75.01284728020843, 'title':"Akaluj"},
            {'lat': 18.089874508302604, 'lng': 75.42069391501146, 'title':"kurduwadi"},
            {'lat': 18.14354759945392, 'lng': 75.63185328384088, 'title':"Barshi"},
            {'lat': 18.109979946988947, 'lng': 75.01842141450722, 'title':"Indapur"},
            {'lat': 18.255052721419432, 'lng': 75.16703601621819, 'title':"Jejur"},
            {'lat': 18.308551716064127, 'lng': 75.14662192257657, 'title':"Kumbhej"},
            {'lat': 18.40545804204036, 'lng': 75.20325909818195, 'title':"Karmala"},
            {'lat': 18.596007974655144, 'lng': 75.30834549083511, 'title':"Nannaj"},
           
            # Add more data as needed
        ]

        for data in places_data:
            Place2.objects.create(lat=data['lat'], lng=data['lng'], title=data['title'])

        self.stdout.write(self.style.SUCCESS('Successfully fed the Place table'))
