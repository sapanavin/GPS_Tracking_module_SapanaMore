import random
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
import googlemaps
from datetime import datetime
from .models import Place, Place2 

# def map(request):
#     key = settings.GOOGLE_API_KEY
#     context = {
#         'key':key,
#     }
#     return render(request, 'maps_google/map.html',context)

def get_directions(request):
    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')

        # Initialize Google Maps API client
        gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)

        # Get directions
        directions_result = gmaps.directions(origin, destination, mode="driving", departure_time=datetime.now())

        if directions_result:
            route = directions_result[0]
            distance = route['legs'][0]['distance']['text']
            duration = route['legs'][0]['duration']['text']
            start_location = route['legs'][0]['start_location']
            end_location = route['legs'][0]['end_location']
            print(start_location)
            print(end_location)

         

            context = {
                'key' : settings.GOOGLE_API_KEY,
                'origin': origin,
                'destination': destination,
                'distance': distance,
                'duration': duration,
                'route': route,
                'start_location' : start_location,
                'end_location' : end_location,
                'display' : 100
                
            }
            # print(context)

            return render(request, 'directions/directions_result.html', context)

    context = {
                'key' : settings.GOOGLE_API_KEY,
                'display' : -100
               
    }
    return render(request, 'directions/get_directions.html', context)


def dynamic_places(request):
     # Retrieve places from the database
    generate_sample_data()#this method generates dynamic lat and lng and save into the database
    places_queryset = Place.objects.all()

    # Convert queryset to a list of dictionaries
    places_list = [{'lat': place.lat, 'lng': place.lng} for place in places_queryset]
    print("Places_list from mark_places : ", places_list)
    # Optionally, you can return JSON response instead of rendering a template
    # return JsonResponse({'places': places_list})
    context = {'places': places_list,
               'Length' :len(places_list)}
    
    return render(request, 'directions/dynamic_places.html', context)

def custom_places(request):
     # Retrieve places from the database
    places_queryset = Place2.objects.all()

    # Convert queryset to a list of dictionaries
    places_list = [{'lat': place.lat, 'lng': place.lng, 'title': place.title} for place in places_queryset]
    print(places_list)
    # Optionally, you can return JSON response instead of rendering a template
    # return JsonResponse({'places': places_list})
    context = {'places': places_list,
                 'Length' :len(places_list)}
    
    return render(request, 'directions/custom_places.html', context)

def generate_sample_data(num_points=10):
    for _ in range(num_points):
        # Generate random latitude and longitude coordinates
        latitude = round(random.uniform(19, 20 ), 6)
        longitude = round(random.uniform(73, 74), 6)

        # Save the data to the database
        Place.objects.create(lat=latitude, lng=longitude)


def ashtavinayak(request):
    return render(request, 'directions/ashtavinayak.html')