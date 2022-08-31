from load_data import load_busstps, load_vehicles_data, load_bus_ride
from location import find_location, calculate_the_distance_from_the_stops
from map import creatinMap
from trip_recommend import recommend_trip
from user_function import select_number_linie, place_start_trip, place_end_trip, print_info_about_trip, \
    print_no_bus_info

WALK_DISTANCE_IN_M = 450
def set_the_route():
    stops = load_busstps()
    addres = place_start_trip()
    start_palce = find_location(addres)
    src_bus_stops = calculate_the_distance_from_the_stops(start_palce, WALK_DISTANCE_IN_M, stops)
    addres_end = place_end_trip()
    end_palce = find_location(addres_end)
    stops_from_end_place = calculate_the_distance_from_the_stops(end_palce, WALK_DISTANCE_IN_M, stops)
    # pobranie wszystkich pojazdów
    vehicles = load_vehicles_data()
    # lista przystanków dla konkretnej linii
    select_numer_vehicals = select_number_linie()
    bus_rides = load_bus_ride(select_numer_vehicals)
    # określona trasa
    trip = recommend_trip(src_bus_stops, stops_from_end_place, bus_rides)
    if trip:
        creatinMap(vehicles, trip)
        print_info_about_trip(trip)
    else:
        print_no_bus_info()

if __name__ == '__main__':
    set_the_route()
