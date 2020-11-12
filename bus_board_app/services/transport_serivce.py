import collections
import requests
import json
import datetime
#class TransportService():
#    def __init__(self, app_id, app_key):
app_id = 'a5ecfe79'
app_key = '2b4c04d18256dda4a7310b23082bba8b'
    

def getLiveBusForATCO(atco = "490008660N"):

    request_url = "http://transportapi.com/v3/uk/bus/stop/"+atco+"/live.json?app_id="+app_id+"&app_key="+app_key

    result = requests.get(request_url)
    data = json.loads(result.text)
    #requestTime = datetime.datetime.strptime(data["request_time"], "%Y-%m-%dT%H:%M%S+hh:mm")
    requestTime = data["request_time"]
    stopName = data["stop_name"]
    departures = data["departures"]

    today = datetime.datetime.today()
    # print(departures)
    buses = []
    for key, value in departures.items():
        for bus in value:
            expected_datetime = bus["expected_departure_date"] + " " + bus["expected_departure_time"]
            date_time_obj = datetime.datetime.strptime(expected_datetime, "%Y-%m-%d %H:%M")
            timeDiff = date_time_obj - today
            # print(timeDiff)
            bus["timeDiff"]=int(timeDiff.total_seconds()/60)
            buses.append(bus)
    return (requestTime,stopName,buses)


def get_nearest_stops(coords):
    request_url = "http://transportapi.com/v3/uk/places.json?lat={latitude}&lon={longitude}&type=bus_stop&app_id={app_id}&app_key={app_key}"
    #request_url.format(coords.longitude, coords.lattitude, app_id, app_key)
