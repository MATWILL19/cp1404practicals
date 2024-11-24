"""CP1404Practical - Unreliable car"""
from prac_09.car import Car
import random

class Unreliablecar(Car):
    """Represent an unreliable Car object."""

    def __init__(self, name, fuel, reliability):
        """Initialise an unreliable car instance"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive an unreliable car"""
        failure_distance = random.randint(0, 100)
        if failure_distance > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
