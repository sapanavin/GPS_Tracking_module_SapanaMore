from django.urls import path

from . import views

# app_name = "directions"
urlpatterns = [
  
     path("", views.get_directions, name="get_directions"),
     path("ashtavinayak", views.ashtavinayak, name="ashtavinayak"),
     path("custom_places", views.custom_places, name="custom_places"),
     path("dynamic_places", views.dynamic_places, name="dynamic_places")
    
]
