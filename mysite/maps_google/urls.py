from django.urls import path

from maps_google import views as view
#from views import HomeView

urlpatterns = [
    path("mymaps", view.my_maps, name="index"),


    path('map',view.map, name="map"),
    path('',view.home, name="home"),
    path('mydata',view.mydata, name="mydata"),
    path('distance',view.distance, name="distance"),
    path('geocode',view.geocode, name="geocode"),
    path('geocode/club/<int:pk>',view.geocode_club, name="geocode_club"),
    path('create_profile/', view.create_profile, name='create_profile'),
    path('success/<int:pk>/', view.success, name='success'),
    path('all_profiles/', view.all_profiles, name='all_profiles')

]