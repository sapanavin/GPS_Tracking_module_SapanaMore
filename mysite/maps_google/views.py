from datetime import datetime
from django.shortcuts import redirect, render
from django.views.generic import ListView
import googlemaps
import json
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from .forms import UserProfileForm

from maps_google.models import FootballClubs, Locations, Short_Location, UserProfile


def index(request):
    context={'name':'Sapana More'}
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "maps_google/index.html", context)

def home(request):
    context={'name':'Sapana More'}
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "maps_google/home.html", context)


def geocode(request):
    clubs = FootballClubs.objects.all()
    context = {
        'clubs':clubs,
    }
    return render(request, 'maps_google/geocode.html',context)


def geocode_club(request,pk):
    club = FootballClubs.objects.get(id=pk)
    # check whether we have the data in the database that we need 
    if club.adress and club.country and club.zipcode and club.city != None: 
        # creating string of existing location data in database
        adress_string = str(club.adress)+", "+str(club.zipcode)+", "+str(club.city) +", "+str(club.country)

        # geocode the string
        gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
        intermediate = json.dumps(gmaps.geocode(str(adress_string))) 
        intermediate2 = json.loads(intermediate)
        latitude = intermediate2[0]['geometry']['location']['lat']
        longitude = intermediate2[0]['geometry']['location']['lng']
     
        # save the lat and long in our database
        club.latitude = latitude
        club.longitude = longitude
        club.save()
        return redirect('geocode')
    else:
        return redirect('geocode')
    return render(request, 'maps_google/empty.html',context)


def distance(request):
    gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
    now = datetime.now()
    calculate = json.dumps(gmaps.distance_matrix("Rat Verlegh Stadion",
                            "Breda Station",
                            mode="driving",
                            departure_time=now)) 
    calculate2 = json.loads(calculate)
    
    result = calculate2
    print(result)
    distance = calculate2['rows'][0]['elements'][0]['distance']['text']
    duration = calculate2['rows'][0]['elements'][0]['duration']['text']

    context = {
        'result':result,
        'distance':distance,
        'duration':duration
    }
    return render(request, 'maps_google/distance.html',context)

def map(request):
    key = settings.GOOGLE_API_KEY
    context = {
        'key':key,
    }
    return render(request, 'maps_google/map.html',context)

def mydata(request):
    result_list = list(FootballClubs.objects\
                .exclude(latitude__isnull=True)\
                .exclude(longitude__isnull=True)\
                .exclude(latitude__exact='')\
                .exclude(longitude__exact='')\
                .values('id',
                        'name', 
                        'latitude',
                        'longitude',
                        'attendance',
                        'stadium',
                        'country',
                        ))
  
    return JsonResponse(result_list, safe=False)

def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('success', pk=instance.id)  # Redirect to the success page with the user's profile ID
    else:
        form = UserProfileForm()

    return render(request, 'maps_google/create_profile.html', {'form': form})

def success(request, pk):
    user_profile = UserProfile.objects.get(pk=pk)
    return render(request, 'maps_google/success.html', {'user_profile': user_profile})

def all_profiles(request):
    user_profiles = UserProfile.objects.all()
    return render(request, 'maps_google/all_profiles.html', {'user_profiles': user_profiles})
def my_maps(request):
    context={'name':'Sapana More'}
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, "maps_google/my_maps.html", context)