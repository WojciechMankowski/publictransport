from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from classes_to_dowlaond import StopsInSequence, BusStop, BusRide
from load_data import load_bus_ride, load_busstps
from location import find_location, calculate_the_distance_from_the_stops


@dataclass
class TripProposal:
    line_number: str
    stops_on_trip: List[StopsInSequence]

    def __str__(self):
        return f"{self.line_number}: {self.stops_on_trip}"
    @property
    def src_stop(self) -> StopsInSequence:
        # print(self.stops_on_trip)
        return self.stops_on_trip[0]

    @property
    def dst_stop(self) -> StopsInSequence:
        return self.stops_on_trip[-1]

    @property
    def departure(self) -> datetime.time:
        return self.src_stop.time

    @property
    def arrival(self) -> datetime.time:
        return self.dst_stop.time


def recommend_trip(
    src_stops: List[BusStop], dst_stops: List[BusStop], bus_rides: List[BusRide]) -> Optional[TripProposal]:
    for ride in bus_rides:
        for stop in src_stops:
            src_stop_on_ride = ride.stop_by_id(stop.id)
            if not src_stop_on_ride:
                continue
            for dst_stop in dst_stops:
                dst_stop_on_ride = ride.stop_by_id(dst_stop.id)

                if not dst_stop_on_ride:
                    continue

                if src_stop_on_ride.order["order"] > dst_stop_on_ride.order["order"]:
                    continue
                stops_start_index = ride.stops.index(src_stop_on_ride)
                stops_end_index = ride.stops.index(dst_stop_on_ride) + 1
                # print(ride.stops[stops_end_index])
                stops_on_trip = ride.stops[stops_end_index:stops_start_index]
                # print(f"stops_on_trip: {stops_on_trip}")
                if len(stops_on_trip) != 0:
                    trip_proposal = TripProposal(line_number=ride.line_number, stops_on_trip=stops_on_trip)
                if trip_proposal.departure > datetime.now().time():
                    return trip_proposal



if __name__ == '__main__':
    busrides = load_bus_ride("12")
    stops = load_busstps()
    addres = "Majkowskiego 8 Gdańsk"
    start_palce = find_location(addres)
    stops_from_start_palce = calculate_the_distance_from_the_stops(start_palce, 200, stops)
    rec = recommend_trip(stops, stops_from_start_palce, busrides)
    print(rec)