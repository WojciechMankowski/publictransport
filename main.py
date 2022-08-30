from load_data import load_busstps
from location import find_location, calculate_the_distance_from_the_stops

addres = "Majkowskiego 8 Gdańsk"
start_palce= find_location(addres)
stops = load_busstps()
stops_from_start_palce=  calculate_the_distance_from_the_stops(start_palce, 200, stops)

addres_end = "Aleja Grunwaldzka 238A, 80-266 Gdańsk"
end_palce = find_location(addres_end)
stops_from_end_place = calculate_the_distance_from_the_stops(end_palce, 300, stops)

