# classe avião

from enum import Enum
from uuid import uuid4

class AirplaneModel(Enum):
    BOEING_737 = "Boeing 737"
    AIRBUS_A320 = "Airbus A320"
    EMBRAER_E195 = "Embraer E195"
    BOEING_777 = "Boeing 777"
    AIRBUS_A380 = "Airbus A380"

class AirplaneRange(Enum):
    NATIONAL = "national"
    INTERNATIONAL = "international"

class Airplane:
    def __init__(self, model: AirplaneModel, range: AirplaneRange, max_capacity: 250):
        self._id = uuid4()
        self._model = model
        self._range = range
        self._max_capacity = max_capacity
    
    @property
    def id(self):
        return self._id

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value: AirplaneModel):
        if not isinstance(value, AirplaneModel):
            raise ValueError("Model must be an instance of AirplaneModel Enum")
        self._model = value
    
    @property
    def range(self):
        return self._range
    
    @range.setter
    def range(self, value: AirplaneRange):
        if not isinstance(value, AirplaneRange):
            raise ValueError("Range must be an instance of AirplaneRange Enum")
        self._range = value
    
    @property
    def max_capacity(self):
        return self._max_capacity
    
    @max_capacity.setter
    def max_capacity(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Max capacity must be a positive integer")
        self._max_capacity = value
    
    def __str__(self) -> str:
        return f"Airplane(id={self.id}, model={self.model.value}, range={self.range.value}, max_capacity={self.max_capacity})"
    