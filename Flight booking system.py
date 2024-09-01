class FlightSearch:
    def __init__(self, flights):
        self.flights = flights
 
    def search_flights(self, airline=None):
        return [flight for flight in self.flights if airline is None or flight.airline == airline]


class Booking:
    def __init__(self, flight, customer):
        self.flight = flight
        self.customer = customer

    def verify_booking(self):
        if self.flight.book_seat():
            print(f"Booking has been verified for {self.customer.name}. Flight is {self.flight.flight_number} to {self.flight.destination}")
        else:
            print("No seats available")


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Flight:
    def __init__(self, flight_number, price, airline, destination, available_seats):
        self.flight_number = flight_number
        self.price = price
        self.airline = airline
        self.destination = destination
        self.available_seats = available_seats
        
    def is_seat_available(self):
        return self.available_seats > 0

    def book_seat(self):
        if self.is_seat_available():
            self.available_seats -= 1
            return True
        return False

if __name__ == "__main__":
    flights = [
      Flight("A1", 120, "Airline A", "Tokyo", 13),
      Flight("B2", 180, "Airline B", "Paris", 9),
      Flight("C3", 150, "Airline C", "New York", 5)
]

    while True:
       print(f"Flight A1 costs $120 and contains {flights[0].available_seats} available seats\n")
       print(f"Flight B2 costs $180 and contains {flights[1].available_seats} available seats\n")
       name= input("Enter your name\n")
       destination = input("Pick a destination (Tokyo, Paris, New York) or type 'exit' to quit: ").strip()
       if destination.lower() == 'exit':
            print("Thanks for using our services")
            exit()
       selection= input("pick flight A1 or flight B2 or type 'exit'\n")
       if selection.lower() == 'exit':
            print("Thanks for using our services")
            exit()
       available_flights = []
       if selection=='A1' :
          flight_search = FlightSearch(flights)
          available_flights = flight_search.search_flights(airline="Airline A")
       elif selection=='B2' :
          flight_search = FlightSearch(flights)
          available_flights = flight_search.search_flights(airline="Airline B")
       if available_flights:
          selected_flight = available_flights[0]
          customer = Customer(name, "customer@example.com")
          booking = Booking(selected_flight, customer)
          booking.verify_booking()
       else:
          print("No flights available")
