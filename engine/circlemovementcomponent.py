from typing import Tuple
from .component import Component
import math


class CircleMovementComponent(Component):
    def __init__(self, radius, center: Tuple, speed, starting_angle, actor=None):
        super().__init__(actor)
        self.radius = radius
        self.center = center
        self.angle = starting_angle  # must be a number between 0 and 360
        # Since we don't have a stablished fps the speed is subjected to the
        # Machine calculation power
        self.speed = speed  # Should be a number between -1 and 1

    def render(self, surface):
        pass

    def update(self):
        if self.angle > 360:
            # Clockwise circle reset
            self.angle -= 360
        elif self.angle < 0:
            # AntiClockwise circle reset
            self.angle += 360

        # Calculating the new coordinates
        radius = math.radians(self.angle)
        self.owner.x = self.center[0] + self.radius * math.cos(radius)
        self.owner.y = self.center[1] + self.radius * math.sin(radius)

        # Adding the speed to the angle
        self.angle += self.speed

    @staticmethod
    def loadFromDict(componentDescriptor):
        radius = componentDescriptor["radius"]
        center = (componentDescriptor["center_x"], componentDescriptor["center_y"])
        speed = componentDescriptor["speed"]
        starting_angle = componentDescriptor["starting_angle"]
        return CircleMovementComponent(radius, center, speed, starting_angle)
