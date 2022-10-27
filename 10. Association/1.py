class Elevator:
    def __init__(self, top_floor, bottom_floor=0, current_floor=0):
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


elevator1 = Elevator(7)
elevator1.go_to_floor(5)
elevator1.go_to_floor(0)

