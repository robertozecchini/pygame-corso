from .component import Component
import pygame

class StaticSpriteComponent(Component):
    def __init__(self, assetFileName, name, actor):
        super().__init__(name, actor)
        self.assetFileName = assetFileName
        self.image = None

    def load(self):
        self.image = pygame.image.load(self.assetFileName)

    def render(self, surface):
        rect = self.image.get_rect()
        rect.centerx = self.owner.x
        rect.centery = self.owner.y
        surface.blit(self.image, rect)


