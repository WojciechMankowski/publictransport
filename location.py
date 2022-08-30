from dataclasses import dataclass
from typing import List

from geopy import Nominatim
from geopy.distance import distance

from classes_to_dowlaond import BusStop
from load_data import load_busstps


@dataclass
class Location:
    address: str
    latitude: float
    longitude: float

    @property
    def location(self):
        return self.latitude, self.longitude


def find_location(address: str) -> Location:
    geolocator = Nominatim(user_agent="webinar-agent")
    address_code = geolocator.geocode(address)
    return Location(address=address, latitude=address_code.latitude, longitude=address_code.longitude)
def calculate_the_distance_from_the_stops(place: Location, distance_in_metr: int, stops: List[BusStop] ):
    good_stops = []
    for bus_stop in stops:
        if distance(place.location, bus_stop.location).meters <= distance_in_metr:
            good_stops.append(bus_stop)
    return good_stops
if __name__ == '__main__':
    addres = "Majkowskiego 8 Gdańsk"
    obj = find_location(addres)
    stops = load_busstps()
    lisT=  calculate_the_distance_from_the_stops(obj, 400, stops)
    print(lisT)