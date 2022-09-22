# continuing improve Car-class
class Car:
    def __init__(self, register, top_speed):
        self.register = register
        self.top_speed = top_speed
        self.current_speed = 0
        self.km_meter = 0

    def speed(self, dispatch):
        if 0 <= self.current_speed + dispatch <= self.top_speed:
            self.current_speed += dispatch
        elif self.current_speed + dispatch > self.top_speed:
            self.current_speed = self.top_speed
        elif self.current_speed + dispatch < 0:
            self.current_speed = 0


# main program to test the class
volvo = Car("ABC-123", 142)
print(f"register: {volvo.register:s}\n"
      f"top speed: {volvo.top_speed:d}km/h"
      f"current speed: {volvo.current_speed:d}km/h\n"
      f"travelled: {volvo.km_meter:d}km.")
volvo.speed(70)
volvo.speed(30)
volvo.speed(50)
print(f"current speed:{volvo.current_speed:d}km/h")
volvo.speed(-200)
print(f"current speed:{volvo.current_speed:d}km/h")