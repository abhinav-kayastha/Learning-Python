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
        for elevator in range(number_of_elevators + 1):
            ele = Elevator()
            self.number_of_elevators.append(ele)

    def run_elevator(self, chosen_elevator, destination_floor):
        if chosen_elevator > len(self.number_of_elevators):
            chosen_elevator = self.number_of_elevators[-1]
            chosen_elevator.go_to_floor(destination_floor)
        elif chosen_elevator < len(self.number_of_elevators):
            chosen_elevator = self.number_of_elevators[0]
            chosen_elevator.go_to_floor(destination_floor)
        else:
            chosen_elevator = self.number_of_elevators[chosen_elevator]
            chosen_elevator.go_to_floor(destination_floor)
        return


building1 = Building(7, 0, 3)
building1.run_elevator(2, 6)
