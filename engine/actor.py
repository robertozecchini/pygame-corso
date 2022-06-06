class Actor:

    def __init__(self):
        self.components = []

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