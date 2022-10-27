class Elevator:
    def __init__(self, top_floor=7, bottom_floor=0, current_floor=0):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = current_floor

    def floor_up(self):
        self.current_floor += 1
        return

    def floor_down(self):
        self.current_floor -= 1
        return

    def go_to_floor(self, floor):
        while self.current_floor < floor:
            self.floor_up()
            print(f"Current Floor: {self.current_floor}")
        while self.current_floor > floor:
            self.floor_down()
            print(f"Current Floor: {self.current_floor}")
        return


class Building:
    def __init__(self, top_floor, bottom_floor, number_of_elevators):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.number_of_elevators = []
        for elevator in range(number_of_elevators):
            ele = Elevator()
            self.number_of_elevators.append(ele)

    def run_elevators(self, destination_floor):
        for elevator in self.number_of_elevators:
            elevator.go_to_floor(destination_floor)
            print("\n")
        return

    def fire_alarm(self):
        for elevator in self.number_of_elevators:
            elevator.go_to_floor(0)
            print("\n")
        return


building1 = Building(7, 0, 3)
building1.run_elevators(3)
building1.fire_alarm()