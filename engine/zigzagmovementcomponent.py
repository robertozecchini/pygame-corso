from .component import *
import time
import random


class ZigZagMovementComponent(Component):
    def __init__(self, boundingRect, actor=None):
        super().__init__(actor)
        self.vx = 0.05
        self.vy = 0.05
        self.boundingRect = boundingRect
        self.last_change = time.time()

    def render(self, surface):
        pass

    def random_direction(self):
        # If 1 second is passed since last change the velocity value will randomly change
        if time.time() > self.last_change + 1:
            self.vx = random.randrange(-10, 10) / 10
            self.vy = random.randrange(-10, 10) / 10
            self.last_change = time.time()

    def update(self):
        self.random_direction()

        # bounce on the x axis
        if self.owner.x < 0 or self.owner.x > self.boundingRect.width:
            self.vx = -self.vx

        # bounce on the y axis
        if self.owner.y < 0 or self.owner.y > self.boundingRect.height:
            self.vy = -self.vy

        self.owner.x += self.vx
        self.owner.y += self.vy

    @staticmethod
    def loadFromDict(componentDescriptor):
        from pygame import rect

        rectDescriptor = componentDescriptor["boundingRect"]
        r = rect.Rect(
            rectDescriptor["x"],
            rectDescriptor["y"],
            rectDescriptor["width"],
            rectDescriptor["height"],
        )
        return ZigZagMovementComponent(r)
