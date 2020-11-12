from json.decoder import JSONDecoder
import requests
import json

def get_lat_and_long_for_postcode(postcode):
    postcode = "NW5 1TL" #TODO : Remove hardcoding
    request_url = "https://api.postcodes.io/postcodes/" + postcode

    response = requests.get(request_url)
    jsonResponse = json.loads(response.text)["result"]

    lati = jsonResponse["latitude"]
    longi = jsonResponse["longitude"]

    responseTuple = (lati, longi)
    return responseTuple
