# passageiros / clientes do avião
from classes.person import Person

class Passenger(Person):
    def __init__(self, name, cpf, seat_number):
        super().__init__(name, cpf)
        if not isinstance(seat_number, int) or seat_number <= 0:
            raise ValueError("Seat number must be a positive integer")
        self._seat_number = seat_number  # Número do assento reservado

    @property
    def seat_number(self):
        return self._seat_number

    def __str__(self):
        return f"Passenger: {self._name}, CPF: {self._cpf}, Seat: {self._seat_number}"
