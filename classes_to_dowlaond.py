from dataclasses import dataclass


@dataclass
class Vehicle:
    number_linie: int
    latitude: float
    longitude: float

    @property
    def location(self):
        return self.latitude, self.longitude

@dataclass
class BusStop:
    id: int
    name_busstop: str
    latitude: float
    longitude: float

    @property
    def location(self):
        return self.latitude, self.longitude
@dataclass
class StopsInSequence(BusStop):
    order: int
    time: datetime.time

@dataclass
class BusRide:
    line_number: str
    stops: list[StopsInSequence]