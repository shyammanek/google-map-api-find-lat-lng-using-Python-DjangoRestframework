import requests
from urllib.parse import urlencode
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dict2xml import dict2xml


@api_view(['GET'])
def get_lat_lng(request, getAddressDetails, flag):
    data_type = "json"
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address": getAddressDetails, "key": "Enter Your API KEY"}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    r = requests.get(url)
    latlng = {}
    try:
        latlng = r.json()['results'][0]['geometry']['location']
        address = r.json()['results'][0]['formatted_address']
        coordinates = {"coordinates": latlng, "address": address, "output_format": ""}
    except:
        pass
    if flag == "xml":
        coordinates = {"coordinates": latlng, "address": address, "output_format": "Xml"}
        xml = dict2xml(coordinates)
        print(xml)
        return Response(xml)
    if flag == "json":
        coordinates = {"coordinates": latlng, "address": address, "output_format": "Json"}
        return Response(coordinates)
