# assentos devem ser (uma lista de itens/assentos dentro da classe avião) 

class Seats:
    def __init__(self, total_seats=250):
        self._total_seats = total_seats  # Total de assentos no avião
        self._available_seats = total_seats  # Assentos disponíveis
        self._reserved_seats = []  # Lista de assentos reservados

    def reserve_seat(self, seat_number):
        if seat_number < 1 or seat_number > self._total_seats:
            raise ValueError("Invalid number seat.")
        if seat_number in self._reserved_seats:
            raise ValueError("Seat already reserved.")
        
        self._reserved_seats.append(seat_number)
        self._available_seats -= 1
        
    def cancel_reservation(self, seat_number):
        if seat_number not in self._reserved_seats:
            raise ValueError("Seat can't be reserved.")

        self._reserved_seats.remove(seat_number)
        self._available_seats += 1

    def get_available_seats(self):
        return self._available_seats
    
    def get_reserved_seats(self):
        return sorted(self._reserved_seats)