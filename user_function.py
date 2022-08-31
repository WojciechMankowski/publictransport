from trip_recommend import TripProposal


def select_number_linie() -> str:
    select_number_linie = input("Jaką linią chcesz jechać? ")
    return select_number_linie

def place_start_trip():
    start_trip = input("Z jakiego miejsca zaczynaż podróż? ")
    return start_trip

def place_end_trip():
    end_trip = input("Gdzie dokładnie chcesz jechać? ")
    return end_trip


def print_info_about_trip(trip: TripProposal):
    src_stop = trip.src_stop.name_busstop
    dst_stop = trip.dst_stop.name_busstop
    line_number = trip.line_number
    departure = trip.departure
    arrival = trip.arrival
    print(f"Rusz o {departure} z przystanku {src_stop}")
    print(f"Jedz numerem {line_number} do przystanku {dst_stop}")
    print(f"Na miejscu będziesz {arrival}")


def print_no_bus_info():
    print("Nie znaleziono połączenia")