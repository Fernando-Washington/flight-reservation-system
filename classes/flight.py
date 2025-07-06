# classe voos 
from uuid import uuid4
from classes.seats import Seats
from classes.price import Price
from classes.airplane import Airplane, AirplaneModel, AirplaneRange
from classes.passenger import Passenger

from resources import *

class Flight:
    def __init__(self, origin, destination, base_price, airplane):
        self._id = uuid4() # Gera um UUID único
        self._origin = origin
        self._destination = destination
        self._airplane = airplane
        self._airplane_crews = {}
        self._passengers = {}
        self._price = Price(base_price, self._id)
        self._seats = Seats(250)  # Cada voo tem 250 lugares
    
    @property
    def seats(self):
        return self._seats

    @property
    def passengers(self):
        return self._passengers

    @property
    def airplane_crews(self):
        return self._airplane_crews

    @property
    def price(self):
        return self._price

    @property
    def origin(self):
        return self._origin

    @property
    def destination(self):
        return self._destination

    @property
    def id(self):
        return self._id

    @property
    def airplane(self):
        return self._airplane

        
    def add_passenger(self, passenger): 
        try:
            self._seats.reserve_seat(passenger.seat_number)
        except ValueError as e:
            raise ValueError(f"Cannot add passenger {passenger.name}: {str(e)}")
        
        self._passengers[passenger.cpf] = passenger
        
    def add_airplane_crew(self, airplane_crew):
        cpf = airplane_crew.cpf
        
        if cpf in self._airplane_crews:
            raise ValueError(f"Airplane crew with CPF {cpf} already exists.")
        
        self._airplane_crews[cpf] = airplane_crew
        
    def create_flights():
        models = list(AirplaneModel)
        ranges = list(AirplaneRange)
        flights = []
        for i in range(10):
            model = random.choice(models)
            range_ = random.choice(ranges)
            origin = f"City_{random.randint(1, 10)}"
            destination = f"City_{random.randint(11, 20)}"
            price = random.randint(300, 2000)
            airplane = Airplane(model, range_, 250)
            flight = Flight(origin, destination, price, airplane)
            flights.append(flight)
        return flights
    
    def add_passengers(flight, quantity=250):
        available_seats = list(set(range(1, 251)) - set(flight.seats.get_reserved_seats()))
        random.shuffle(available_seats)
        for i in range(quantity):
            name = fake.name()
            cpf = clean_cpf(fake.cpf())
            seat = available_seats.pop()
            passenger = Passenger(name, cpf, seat)
            flight.add_passenger(passenger)
            
    def show_flights(flights):
        for idx, flight in enumerate(flights, 1):
            summary = flight.summary()
            print(f"\n--- Flight {idx} ---")
            print(f"ID: {summary['id']}")
            print(f"Origin: {summary['origin']} | Destination: {summary['destination']}")
            print(f"Seat price: R$ {summary['price_per_seat']}")
            print(f"Available seats: {summary['available_seats']}")
            # Show 10 random seats (available or reserved) with passenger name
            all_seats = list(range(1, 251))
            random_seats = random.sample(all_seats, 10)
            print("10 random seats:")
            for seat in random_seats:
                passenger_name = None
                for p in flight.passengers.values():
                    if p.seat_number == seat:
                        passenger_name = p.name
                        break
                if passenger_name:
                    print(f"  Seat {seat}: {passenger_name}")
                else:
                    print(f"  Seat {seat}: Available")
            # Show crew
            print("Crew:")
            for crew in flight.airplane_crews.values():
                print(f"  - {crew.name} ({crew.role})")
            print(f"Total passengers: {summary['passengers_count']}")

        
    def summary(self):
        return {
            "id": str(self._id),
            "origin": self._origin,
            "destination": self._destination,
            "total_seats": self._seats._total_seats,
            "available_seats": self._seats.get_available_seats(),
            "reserved_seats": self._seats.get_reserved_seats(),
            "price_per_seat": self._price.value,
            "passengers_count": len(self._passengers),
            "airplane_crews_count": len(self._airplane_crews)
        }