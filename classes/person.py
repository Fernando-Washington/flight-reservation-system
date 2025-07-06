# tudo o que uma pessoa tem e pode fazer em relação ao voo
# classe abstrata de pessoa para não ser instanciada diretamente
from abc import ABC

class Person(ABC):
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value
        
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        if not value or len(value) != 11 or not value.isdigit():
            raise ValueError("CPF must be a valid 11-digit number")
        self._cpf = value
        
        
            
            