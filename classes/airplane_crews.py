# tripulação do avião
from  classes.person import Person

from resources import *

class AirplaneCrews(Person):
    def __init__(self, name, cpf, role):
        super().__init__(name, cpf)
        self._role = role
        
    @property
    def role(self):
        return self._role
    
    @role.setter
    def role(self, value):
        allowed_roles = ['pilot', 'co-pilot', 'flight attendant']
        value_lower = value.lower()
        if value_lower not in allowed_roles:
            raise ValueError(f"Role must be one of {allowed_roles}")
        self._role = value_lower
    
    def add_airplane_crews(flight):
        roles = ["pilot", "co-pilot", "flight attendant", "flight attendant"]
        for role in roles:
            name = fake.name()
            cpf = clean_cpf(fake.cpf())
            crew = AirplaneCrews(name, cpf, role)
            flight.add_airplane_crew(crew)
