from Vehicle import Vehicle
from VehicleType import VehicleType


class ParkingSlot:
    def __init__(self, floor: int, slotNumber: int):
        self.floor = floor
        self.slotNumber = slotNumber
        self.filled = False
        self.ticketId = None
        self.vehicle = None

        if (slotNumber == 0):
            self.supportType = VehicleType.TRUCK
        elif (slotNumber <= 2):
            self.supportType = VehicleType.BIKE
        else:
            self.supportType = VehicleType.CAR

    def fillVehicle(self, ticketId: str, vehicleType: VehicleType, vehicleRegNo: str, vehicleColor: str):
        self.filled = True
        self.ticketId = ticketId
        self.vehicle = Vehicle(vehicleType, vehicleRegNo, vehicleColor)
