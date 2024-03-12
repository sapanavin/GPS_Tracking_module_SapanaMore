# GPS_Tracking_module_SapanaMore

**http://localhost:8000/directions/**
When user visits this webpage then user need to Origin and Destination places into the Input tags. and as a result Distance, travel time and route will be displayed for the user on the google map.

![image](https://github.com/sapanavin/GPS_Tracking_module_SapanaMore/assets/116043155/62cec92e-2eaa-4362-8421-e82efbb6d318)
**http://localhost:8000/directions/ashtavinayak**
for this webpage I have fed Destinataion and Origin as a Addressess of Ashtavinayak places in Maharashtra. 
So user can get by distance and route between any two Ashtavinayak places by simply selecting Destination and Origin location from pop up. 
![image](https://github.com/sapanavin/GPS_Tracking_module_SapanaMore/assets/116043155/d31d0c4d-d1dd-494d-94f1-bb6a57e9f6ef)
![image](https://github.com/sapanavin/GPS_Tracking_module_SapanaMore/assets/116043155/e14d0435-8a04-44dd-9e3e-3026764db658)



**http://localhost:8000/directions/custom_places:**
for this web Page I have manually given Lat and Lng of following places in database and then every second just move the marker from one location to anothr.
Shikrapur, Daund,Baramati,Indapur, Akaluj, kurduwadi, Barshi, Indapur, Jejur, Kumbhej, Karmala, Nannaj.


**http://localhost:8000/directions/dynamic_places**

For this web page I have dynamically calculated lat and lngusing following expression :
          latitude = round(random.uniform(19, 20 ), 6)
          longitude = round(random.uniform(73, 74), 6)
          and then fed the database and move bus marker on map from one location to another per second.
