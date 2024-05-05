import phonenumbers
import opencage
import folium

#users phone number
from myphone import number

from phonenumbers import geocoder

#prints the parent location 
pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)


#getting the service provider name
from phonenumbers import carrier 
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))


#importing opencage module to get API key
from opencage.geocoder import OpenCageGeocode

key = "f0875e146f16436faefd878413247c53"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

#print(results)
lat = results[0]['geometry']['lat']
lng= results[0]['geometry']['lng']

print(lat, lng)


myMap = folium.Map(location=[lat, lng], zoom_start= 9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

#saving location results as html file 
myMap.save("mylocation.html")