from load_data import load_busstps, load_vehicles_data, load_bus_ride
from location import find_location, calculate_the_distance_from_the_stops
from map import creatinMap
from trip_recommend import recommend_trip


def set_the_route():
    stops = load_busstps()
    addres = "Majkowskiego 8 Gdańsk"
    start_palce = find_location(addres)
    src_bus_stops = calculate_the_distance_from_the_stops(start_palce, 400, stops)

    # addres_end = "pl. Solidarności 1, 80-863 Gdańsk"
    addres_end = "Podwale Grodzkie 2c, 80-895 Gdańsk"
    end_palce = find_location(addres_end)
    stops_from_end_place = calculate_the_distance_from_the_stops(end_palce, 400, stops)
    # pobranie wszystkich pojazdów
    vehicles = load_vehicles_data()
    # lista przystanków dla konkretnej linii
    select_numer_vehicals = input("Jaką linią chcesz jechać? ")
    bus_rides = load_bus_ride(select_numer_vehicals)
    # określona trasa
    trip = recommend_trip(src_bus_stops, stops_from_end_place, bus_rides)
    print(trip)
    if trip:
        creatinMap(vehicles, trip)
        # generate_map(vehicles, trip)
        # print_info_about_trip(trip)
    else:
        print("Błąd")

if __name__ == '__main__':
    set_the_route()
