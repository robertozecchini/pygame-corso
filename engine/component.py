class Component:

    # Owner could be empty at first
    def __init__(self, actor=None):
        self.owner = actor
        self.name = ""

    def load(self):
        pass

    def render(self, surface):
        pass

    # There will be timing involved
    def update(self):
        pass

    def setOwner(self, actor):
        self.owner = actor

    @staticmethod
    def loadFromDict(componentDescriptor):
        import importlib

        module = importlib.import_module(componentDescriptor["module"])
        base_class = getattr(module, componentDescriptor["type"])
        component = base_class.loadFromDict(componentDescriptor)
        return component
