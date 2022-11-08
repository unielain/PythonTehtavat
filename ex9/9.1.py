# a simple program for making a class and testing it


class Car:
    def __init__(self, register, top_speed):
        self.register = register
        self.top_speed = top_speed
        self.current_speed = 0
        self.km_meter = 0

# main program where we test our class


volvo = Car("ABC-123", 142)
print(f"register: {volvo.register:s}\n"
      f"top speed: {volvo.top_speed:d} km/h\n"
      f"current speed: {volvo.current_speed:d} km/h\n"
      f"driven: {volvo.km_meter:d} km.")
