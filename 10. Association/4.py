from random import randint


class Car:

    def __init__(self, registration_number, max_speed, current_speed=0, distance_travelled=0):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.distance_travelled = distance_travelled

    def accelerate(self, change_of_speed):
        self.current_speed = self.current_speed + change_of_speed
        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        return

    def drive(self, hours):
        self.distance_travelled = self.distance_travelled + (hours * self.current_speed)
        return


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car_change_in_speed = randint(-10, 15)

            if 0 < car.current_speed + car_change_in_speed < car.max_speed:
                car.current_speed += car_change_in_speed
                car.drive(1)
            elif car.current_speed + car_change_in_speed > car.max_speed:
                car.current_speed = car.max_speed
                car.drive(1)
        return

    def print_status(self):
        for car in self.cars:
            print(
                f"Name: {car.registration_number}, Max Speed: {car.max_speed}, Current Speed: {car.current_speed}, Distance Travelled: {car.distance_travelled}")
        return

    def race_finished(self):
        for car in self.cars:
            if car.distance_travelled >= self.distance:
                return True
        return


# Main program
cars = []

porsche = Car("Porsche", 200)
lamborghini = Car("Aventador", 200)

cars.append(porsche)
cars.append(lamborghini)

race = Race("Grand Demolition Derby", 8000, cars)


while True:
    race.hour_passes()
    race.print_status()
    if race.race_finished():
        break


