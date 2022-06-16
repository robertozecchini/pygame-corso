import pygame, pygame.locals, sys
from engine.scene import *
from engine.component import *
from engine.actor import *
from engine.staticspritecomponent import *
from engine.bouncingmovementcomponent import *
from engine.scenefactory import *
import copy

pygame.init()

# Global state variable
Quit = False

# Level setup code
scene = SceneFactory.loadSceneFromFile("example.json")

#New scene that need to be save
newScene = Scene()
newScene.windowRect.width = 800
newScene.windowRect.height = 600

actor = Actor()
actor.addComponent(StaticSpriteComponent("assets/ghost1.png"))
actor.addComponent(BouncingMovementComponent(pygame.Rect(10, 10, 300, 400)))

actor2 = Actor()
actor2.addComponent(StaticSpriteComponent("assets/ghost2.png"))
actor2.addComponent(BouncingMovementComponent(pygame.Rect(50, 80, 500, 800)))

newScene.actors.append(actor)
newScene.actors.append(actor2)

SceneFactory.saveSceneToFile(newScene, "pippo.json")
# setup the window
window = pygame.display.set_mode((scene.windowRect.width, scene.windowRect.height), 0, 32)
pygame.display.set_caption("Titolo bellissimo")
scene.load()


def process_events():
    global Quit
    # process all the events generated by the system
    for event in pygame.event.get():
        # event QUIT is generated when the user closes the application window
        if event.type == pygame.locals.QUIT:
            Quit = True

def update_game_logic():
    global scene
    
    scene.update()

    return

def render():
    global scene

    # clear the screen
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    window.fill(BLACK)

    scene.render(window)
    
    # update the display with the new content of the window
    pygame.display.update()

# game loop
while not Quit:
    process_events()
    
    update_game_logic()
    
    render()

pygame.quit()
sys.exit()