class Actor:
    def __init__(self):
        self.components = []
        self.x = 0
        self.y = 0
        self.name = ""

    def load(self):
        for a in self.components:
            a.load()

    def render(self, surface):
        for a in self.components:
            a.render(surface)

    # There will be timing involved
    def update(self):
        for a in self.components:
            a.update()

    def addComponent(self, component):
        self.components.append(component)
        component.setOwner(self)

    def loadFromDict(self, actorDescriptor):
        self.name = actorDescriptor["name"]
        self.x = actorDescriptor["x"]
        self.y = actorDescriptor["y"]

    def saveToDict(self):
        savedict = {
            "name": str(self.name),
            "x": self.x,
            "y": self.y,
        }
        components_dict = []
        for component in self.components:
            components_dict.append(component.saveToDict())
        savedict["components"] = components_dict
        return savedict
