from typing import List
from load_data import load_vehicles_data
import folium
from classes_to_dowlaond import Vehicle
from trip_recommend import TripProposal

GDANSK_LOCATION = (54.3382, 18.60874)
def creatinMap(vehicles: List[Vehicle], trip: TripProposal):
    trip_map = folium.Map(location=GDANSK_LOCATION, zoom_start=12)
    number_linie = trip.line_number
    src_bus_stop = trip.src_stop
    dst_bus_stop = trip.dst_stop

    for vehicle in vehicles:
        if vehicle.number_linie == number_linie:
            vehicle_info = f"Linia numer {vehicle.number_linie}"
            _create_circle_marker(vehicle.location, color="red", popup=vehicle_info).add_to(trip_map)

    stops_locations = [stop.location for stop in trip.stops_on_trip]
    folium.PolyLine(locations=stops_locations, color="red", weight=3, opacity=1).add_to(trip_map)

    for trip_stop in trip.stops_on_trip:
        _create_circle_marker(trip_stop.location, color="blue", popup=trip_stop.name_busstop).add_to(trip_map)

    _create_circle_marker(src_bus_stop.location, color="blue", popup=src_bus_stop.name_busstop).add_to(trip_map)
    _create_circle_marker(dst_bus_stop.location, color="green", popup=dst_bus_stop.name_busstop).add_to(trip_map)

    trip_map.save("trip_map.html")


def _create_circle_marker(location, color, popup) -> folium.CircleMarker:
    return folium.CircleMarker(
        location=location, popup=popup, color=color, fill_color=color,
        radius=7, fill=True, fill_opacity=1,
    )
if __name__ == '__main__':
    vehicals = load_vehicles_data()
    creatinMap(vehicals, "12")