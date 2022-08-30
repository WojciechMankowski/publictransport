import dataclasses
import math
from datetime import datetime
from typing import List
from requests import get
from classes_to_dowlaond import BusStop, StopsInSequence, BusRide, Vehicle

VEHICLES_DATA_URL = "https://ckan2.multimediagdansk.pl/gpsPositions"

def load_vehicles_data() -> List[Vehicle]:
    vehicles_response = get(VEHICLES_DATA_URL)
    vehicles_data = vehicles_response.json()

    return [
        Vehicle(number_linie=vehicle_info["Line"], latitude=vehicle_info["Lat"], longitude=vehicle_info["Lon"], )
        for vehicle_info in vehicles_data["Vehicles"]
    ]

def load_busstps():
    url = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/4c4025f0-01bf-41f7" \
          "-a39f-d156d201b82b/download/stops.json "
    res = get(url).json()
    current_date = datetime.now().date()
    json_busstops = res[str(current_date)]
    return [
        BusStop(
            id=busstop['stopId'],
            name_busstop=busstop['stopName'],
            latitude=busstop['stopLat'],
            longitude=busstop["stopLon"]
        ) for busstop in json_busstops["stops"]
    ]


def load_bus_ride(numebr_line):
    all_bus_stop = load_busstps()
    all_bus_stop_id = {busstop.id: busstop for busstop in all_bus_stop}

    date = f"{datetime.now().date()}"
    url = "https://ckan.multimediagdansk.pl/dataset/c24aa637-3619-4dc2-a171-a23eec8f2172/resource/a023ceb0-8085-45f6" \
          "-8261-02e6fcba7971/download/stoptimes.json "
    response = get(url).json()
    json_data = response[numebr_line]

    for _url in json_data:
        text = _url[49:]
        text = text[:10]
        if text == date:
            url = _url
    previous_stop_order = math.inf
    bus_rides = []
    schedule_data = get(url).json()["stopTimes"]
    for stop_info in schedule_data:
        orders = stop_info["stopSequence"]
        if orders < previous_stop_order:
            ride: BusRide = BusRide(line_number=numebr_line, stops=[])
            bus_rides.append(ride)
        stop_id = stop_info["stopId"]
        base_bus_date = all_bus_stop_id[stop_id]
        time = datetime.strptime(stop_info["departureTime"], "%Y-%m-%dT%H:%M:%S").time()
        bus_stop_on_ride = StopsInSequence(id=base_bus_date.id, name_busstop=base_bus_date.name_busstop,
                                           latitude=base_bus_date.latitude, longitude=base_bus_date.longitude,
                                           order=orders, time=time, )
        ride.stops.append(bus_stop_on_ride)

        previous_stop_order = orders

    return bus_rides
