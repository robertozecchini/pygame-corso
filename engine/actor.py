class Actor:

    def __init__(self, scene):
        self.components = []
        self.x = 0
        self.y = 0
        self.name = ""
        self.scene = scene

    def load(self):
        for a in self.components:
            a.load()

    def render(self, surface):
        for a in self.components:
            a.render(surface)

    # There will be timing involved
    def update(self, deltaTime):
        for a in self.components:
            a.update(deltaTime)
            
    def addComponent(self, component):
        self.components.append(component)
        component.setOwner(self)

