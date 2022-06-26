import json
from engine.scene import *
from engine.component import *
from engine.actor import *
from engine.staticspritecomponent import *
from engine.bouncingmovementcomponent import *
from .floatingmovementcomponent import *
from .pathmovementcomponent import *
from pygame import rect

class SceneFactory:

    def loadSceneFromFile(fileName):
        with open(fileName, "r") as f:
            try:
                # this is a dictionary
                sceneDescriptor = json.load(f)

                scene = Scene()
                windowDescriptor = sceneDescriptor["window"]
                scene.windowRect.height = windowDescriptor["height"]
                scene.windowRect.width = windowDescriptor["width"]
                scene.title = windowDescriptor["title"]
                
                for actorDescriptor in sceneDescriptor["actors"]:
                    actor = Actor(scene)
                    actor.name = actorDescriptor["name"]
                    actor.x = actorDescriptor["x"]
                    actor.y = actorDescriptor["y"]
                    
                    for componentDescriptor in actorDescriptor["components"]:
                        component = None
                        if componentDescriptor["type"] == StaticSpriteComponent.__name__:
                            component = StaticSpriteComponent(componentDescriptor["fileName"], componentDescriptor["name"], actor)
                        elif componentDescriptor["type"] == BouncingMovementComponent.__name__:
                            rectDescriptor = componentDescriptor["boundingRect"]
                            r = rect.Rect(rectDescriptor["x"], rectDescriptor["y"],
                                rectDescriptor["width"], rectDescriptor["height"])
                            component = BouncingMovementComponent(componentDescriptor["name"], r, actor)
                        elif componentDescriptor["type"] == FloatingMovementComponent.__name__:
                            component = FloatingMovementComponent(componentDescriptor["name"], actor)
                        elif componentDescriptor["type"] == PathMovementComponent.__name__:
                            component = PathMovementComponent(componentDescriptor["name"], actor, componentDescriptor["path"])
                        else:
                            raise Exception(f"Wrong component type: {componentDescriptor['type']}")
                        
                        actor.addComponent(component)
                    
                    scene.actors.append(actor)
                return scene
                
            except Exception as e:
                print(f"Error on filename : {fileName}")
                print(str(e))