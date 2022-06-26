class Component:

    # Owner could be empty at first
    def __init__(self, name, actor):
        self.name = name
        self.owner = actor

    def load(self):
        pass

    def render(self, surface):
        pass

    # There will be timing involved
    def update(self, deltaTime):
        pass

    def setOwner(self, actor):
        self.owner = actor