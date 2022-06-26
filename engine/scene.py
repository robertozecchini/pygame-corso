from pygame import rect

class Scene:

    def __init__(self):
        # there will be actors acting things
        self.actors = []
        self.windowRect = rect.Rect(0,0,0,0)
        self.title = ""

    def load(self):
        for a in self.actors:
            a.load()

    def render(self, surface):
        for a in self.actors:
            a.render(surface)

    def update(self, deltaTime):
        for a in self.actors:
            a.update(deltaTime)