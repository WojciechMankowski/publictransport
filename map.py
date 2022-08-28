from typing import List
from load_data import load_vehicles_data
import folium
from classes_to_dowlaond import Vehicle
GDANSK_LOCATION = (54.3382, 18.60874)
def creatinMap(vehicles: List[Vehicle], number_linie):
    trip_map = folium.Map(location=GDANSK_LOCATION, zoom_start=12)

    for vehicle in vehicles:
        if vehicle.number_linie == number_linie:
            print(vehicle)
            vehicle_info = f"Linia numer {vehicle.number_linie}"
            _create_circle_marker(vehicle.location, color="red", popup=vehicle_info).add_to(trip_map)
    trip_map.save("trip_map.html")
def _create_circle_marker(location, color, popup) -> folium.CircleMarker:
    return folium.CircleMarker(
        location=location, popup=popup, color=color, fill_color=color,
        radius=7, fill=True, fill_opacity=1,
    )
if __name__ == '__main__':
    vehicals = load_vehicles_data()
    creatinMap(vehicals, "12")