import random
# subclasses for class Car


class Car:
    def __init__(self, car_register, top_speed):
        self.car_register = car_register
        self.top_speed = top_speed
        self.current_speed = 0
        self.travel_meter = 0

    def speed(self, dispatch):
        if 0 <= self.current_speed + dispatch <= self.top_speed:
            self.current_speed += dispatch
        elif self.current_speed + dispatch > self.top_speed:
            self.current_speed = self.top_speed
        elif self.current_speed + dispatch < 0:
            self.current_speed = 0

    def travel(self, hours_travelled):
        km_travelled = hours_travelled * self.current_speed
        self.travel_meter += int(km_travelled)

    def get_car_information(self):
        return f"car's register plate: {self.car_register}\n" \
               f"travelled: {self.travel_meter} km"


# ElectricCar and Combustion_engine_car are subclasses for the class Car
class ElectricCar(Car):
    def __init__(self, car_battery_capacity, car_register, top_speed):
        super().__init__(car_register, top_speed)
        self.car_battery_capacity = car_battery_capacity


class CombustionEngineCar(Car):
    def __init__(self, gas_tank, car_register, top_speed):
        super().__init__(car_register, top_speed)
        self.gas_tank = gas_tank


# main program to test classes
tesla = ElectricCar(52.5, "ABC-15", 180)
lada = CombustionEngineCar(32.3, "ACD-123", 165)
tesla.speed(120)
lada.speed(80)
lada.travel(3)
tesla.travel(3)
print(tesla.get_car_information())
print(lada.get_car_information())