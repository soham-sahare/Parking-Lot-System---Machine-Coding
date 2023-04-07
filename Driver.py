from ParkingLot import ParkingLot

import sys

sys.stdin = open("_input.txt", "r")
sys.stdout = open("_output.txt", "w")


class Driver(object):

    def __init__(self):
        self.parking_lots = {}
        self.last_parking_slot = None
        self.run()

    def run(self):

        while(True):

            temp = list(map(str, input().split(" ")))

            if(temp[0] == "exit"):
                break

            elif(temp[0] == "create_parking_lot"):
                id = temp[1]
                floors = temp[2]
                slots = temp[3]

                if(id in self.parking_lots):
                    print("Parking lot already exists")
                    return
                else:
                    print("Created parking lot with " + str(floors) + " floors and " + str(slots) + " slots per floor")
                    self.parking_lots[id] = ParkingLot(id, floors, slots)
                    self.lastParkingSlot = id

            elif(temp[0] == "display"):
                self.parking_lots[self.lastParkingSlot].display(
                    temp[1], temp[2])
            elif(temp[0] == "park_vehicle"):
                self.parking_lots[self.lastParkingSlot].Park(
                    temp[1], temp[2], temp[3])
            elif(temp[0] == "unpark_vehicle"):
                self.parking_lots[self.lastParkingSlot].unPark(temp[1])
            else:
                return

if __name__ == "__main__":
    Driver()
