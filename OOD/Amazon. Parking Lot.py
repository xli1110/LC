"""
A public parking lot has some of parking spots to be used for parking various size cars.
Implement an algorithm for efficiently finding the best possible empty spot for a car.
"""


class Car:
    def __init__(self, car_id, size):
        self.car_id = car_id
        self.size = size  # car size = 1, 2, 3


class ParkingLot:
    def __init__(self):
        self.cars = {}  # key = car_id; val = its lot size
        self.num_lot = [10, 10, 10]  # small, mid, large <=> car_size = 1, 2, 3

    def park(self, car):
        car_size = car.size
        for i in range(len(self.num_lot)):
            if car_size > (i + 1):
                continue
            if self.num_lot[i] > 0:
                self.num_lot[i] -= 1
                self.cars[car.car_id] = i + 1
                break
        raise Exception("Not Enough Space")

    def leave(self, car):
        if car.car_id not in self.cars:
            raise Exception("Car {} has not parked in this parking lot.".format(car.car_id))

        lot_size = self.cars[car.car_id]

        self.num_lot[lot_size - 1] -= 1  # release the slot
        self.cars.pop(car.car_id)  # remove the car_id
