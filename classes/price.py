# cada avião tem um preço diferente por assento
class Price:
    def __init__(self, value, flight_id):
        self._value = value
        self.flight_id = flight_id

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._value = value