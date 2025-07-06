from classes.flight import Flight
from classes.airplane_crews import AirplaneCrews

def main():
    flights = Flight.create_flights()
    for flight in flights:
        AirplaneCrews.add_airplane_crews(flight)
        Flight.add_passengers(flight, quantity=250)
    Flight.show_flights(flights)

if __name__ == "__main__":
    main()