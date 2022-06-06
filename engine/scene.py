class Scene:

    def __init__(self):
        # there will be actors acting things
        self.actors = []

    def load(self):
        for a in self.actors:
            a.load()

    def render(self, surface):
        for a in self.actors:
            a.render(surface)

    # There will be timing involved
    def update(self):
        for a in self.actors:
            a.update()