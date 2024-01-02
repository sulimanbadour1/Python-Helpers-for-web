# Service Oriented Approach
# for example, Google Geocoding API
# http://maps.googleapis.com/maps/api/geocode/json?address=Ann+Arbor%2C+MI


import urllib.request, urllib.parse, urllib.error
import json


serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter location: ")  # Ann Arbor, MI
    if len(address) < 1:
        break

    url = serviceurl + urllib.parse.urlencode(
        {"address": address}
    )  # urlencode() is a function in urllib.parse to be like  "address=Ann+Arbor%2C+MI"
    print("Retrieving", url)

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    print(json.dumps(js, indent=4))  # indent=4 means 4 spaces

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
