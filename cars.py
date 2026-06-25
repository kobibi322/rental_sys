import datetime
from abc import ABC, abstractmethod

class Cars(ABC):
    def __init__(self, category, brand, model, license_plate, color, year, km, seats, price):
        self.category = category
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.color = color
        self.year = year
        self.km = km
        self.seats = seats
        self.price = price
        self.value = self.value_calc()

    def value_calc(self)->int:
        current_year = datetime.datetime.now().year
        year_diff = current_year - self.year
        if self.km > year_diff * 20000:
            km_val = (self.km - year_diff * 20000) * 0.1
        else:
            km_val = 0
        value = (self.price * 0.9 ** year_diff) - km_val
        return int(value)

    @abstractmethod
    def price_calc(self)->int:
        pass

class RentCars(Cars):
    def __init__(self,category, brand, model, license_plate, color, year, km, seats, price):
        super().__init__(category, brand, model, license_plate, color, year, km, seats, price)
        self.price_day = self.price_calc()
        self.km_limit = 250

    def price_calc(self)->int:
        price_day = self.value / 300
        return int(price_day)

class SellCars(Cars):
    def __init__(self,category, brand, model, license_plate, color, year, km, seats, price):
        super().__init__(category, brand, model, license_plate, color, year, km, seats, price)
        self.price = self.price_calc()

    def price_calc(self) -> int:
        price = self.value * 1.1
        return int(price)