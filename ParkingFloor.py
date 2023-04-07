from ParkingSlot import ParkingSlot


class ParkingFloor(object):

    def __init__(self, floors, slots):
        self.floors = {}
        for i in range(0, int(floors)):
            for j in range(0, int(slots)):
                if i not in self.floors:
                    self.floors[i] = {}
                self.floors[i][j] = ParkingSlot(i, j)
