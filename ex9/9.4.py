# a program that uses the Car class to a race
import random
class Car:
    def __init__(self, register, top_speed):
        self.register = register
        self.top_speed = top_speed
        self.current_speed = 0
        self.km_meter = 0

    def speed(self, current_speed):
        if 0 <= self.current_speed + current_speed <= self.top_speed:
            self.current_speed += current_speed
        elif self.current_speed + current_speed > self.top_speed:
            self.current_speed = self.top_speed
        elif self.current_speed + current_speed < 0:
            self.current_speed = 0

    def travel(self, hours):
        travelled = hours * self.current_speed
        self.km_meter += int(travelled)


# functions to factor register plate, top speed, and dispatch
def factor_register(plate_number):
    car_number = str(plate_number)
    register_plate = "ABC-" + car_number
    return register_plate


def factor_top_speed():
    factored_top_speed = random.randrange(100, 200)
    return factored_top_speed


def dispatch_value():
    factored_dispatch = random.randrange(-10, 15)
    return factored_dispatch


# main program with a car race to test the class
cars = []
for i in range(10):
    car = Car(factor_register(i + 1), factor_top_speed())
    cars.append(car)
winner = False
while not winner:
    for car in cars:
        car.speed(dispatch_value())
    for car in cars:
        car.travel(1)
    for car in cars:
        if car.km_meter >= 10000:
            winner = True
            print(f"The winner is: {car.register:s}\n")
            break

# prints the statistics of the car race
title_statistics = "* RACE STATISTICS *"
frame_statistics = "*" * len(title_statistics)
print(f"{frame_statistics}\n"
      f"{title_statistics}\n"
      f"{frame_statistics}")

race_cars = {}
for car in cars:
    race_cars["register"] = car.register
    race_cars["top speed"] = car.top_speed
    race_cars["driven km"] = car.km_meter
    print(race_cars)
