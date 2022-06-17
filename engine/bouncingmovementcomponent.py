from .component import *


class BouncingMovementComponent(Component):
    # Owner could be empty at first
    def __init__(self, boundingRect, actor=None):
        super().__init__(actor)
        self.vx = 0.05
        self.vy = 0.05
        self.boundingRect = boundingRect

    # I could implement some debugging rendering here
    def render(self, surface):
        pass

    # There will be timing involved
    def update(self):
        self.owner.x += self.vx
        self.owner.y += self.vy

        # bounce on the x axis
        if self.owner.x < 0 or self.owner.x > self.boundingRect.width:
            self.vx = -self.vx

        # bounce on the y axis
        if self.owner.y < 0 or self.owner.y > self.boundingRect.height:
            self.vy = -self.vy

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
        return BouncingMovementComponent(r)

    def saveToDict(self):
        savedict = {
            "name": "bouncing",
            "type": "BouncingMovementComponent",
            "module": "engine.bouncingmovementcomponent",
            "boundingRect": {
                        "x" : self.owner.x,
                        "y" : self.owner.y,
                        "width" : self.boundingRect.width,
                        "height" :self.boundingRect.height
            },
            "vx" : self.vx,
            "vy" : self.vy,
        }
        return savedict