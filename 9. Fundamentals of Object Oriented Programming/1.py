class Car:

    def __init__(self, registration_number, max_speed, current_speed=0, distance_travelled=0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled


new_car = Car("ABC-123", 142)

print(f"The car's registration number is {new_car.registration_number}, max speed is {new_car.max_speed} km/h, current speed is {new_car.current_speed} km/h and the distance travelled is {new_car.distance_travelled} km.")