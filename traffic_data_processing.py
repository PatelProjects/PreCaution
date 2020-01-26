# Run $ python3 demo.py in your command line and see events within the last specified timeframe (see startTime and endTime)
from cityiq import CityIq
import time
import json
import requests

# set time frame for use when querying for events (epoch time in milliseconds)
endTime = int(time.time())*1000 # time when demo.py is run
startTime = endTime-(12*3600000) 

# Get current navigation service route from user or automous vehicle. For now, we will use
# google maps but this can be easily configured

req = requests.get("https://maps.googleapis.com/maps/api/directions/json?origin=origin_here&destination=destination_here&key=YOUR_API_KEY")

print("====================================================================================")
print("++++++++++Getting Traffic Data++++++++++++")

print("Getting Traffic Metadata")
# gettting assets - assets with TFEVT events, page 0 
print("Getting Assets")
myCIQ.fetchMetadata("assets","traffic","eventTypes:TFEVT",page=0)
assets = myCIQ.getAssets()

for street in req["geocoded_waypoints"]:
	for camera in assets:
		if street["geocoded_waypoints"]["place_id"] == camera["locationUid"]:
			limitReq = requests.get('https://roads.googleapis.com/v1/speedLimits?placeId=' + 'street["geocoded_waypoints"]["place_id"]' + 'key=YOUR_API_KEY:
				if camera["measures"]["speed"] - 20 < limitReq["speedLimit"]:
					# Sugguest a redirect to google maps (or other navigation system)
					


