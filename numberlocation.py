import phonenumbers

import folium


from phonenumber import number

from phonenumbers import geocoder

key = 'f7bebed25aab4b4eb3be3002f06514ab'

Anynumber = phonenumbers.parse(number)

yourlocation = geocoder.description_for_number(Anynumber, "en")

print(yourlocation)

# get service provider
from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

#getting latitude and longitude

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourlocation)

results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)

mymap = folium.Map(location=[lat, lng], zoom_start = 9)

folium.Marker([lat, lng],popup= yourlocation).add_to((mymap))

# Save it in html file

mymap.save("mylocation.html")