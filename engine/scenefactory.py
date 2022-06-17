import json
from engine.scene import *
from engine.component import *
from engine.actor import *
from engine.staticspritecomponent import *
from engine.bouncingmovementcomponent import *
from pygame import rect


class SceneFactory:
    @staticmethod
    def newloadSceneFromFile(filename):
        with open(filename, "r") as f:
            sceneDescriptor = json.load(f)

            # Loading the main scene
            scene = Scene()
            scene.loadFromDict(sceneDescriptor)

            # Loading each actor in the scene
            for actorDescriptor in sceneDescriptor["actors"]:
                actor = Actor()
                actor.loadFromDict(actorDescriptor)

                # Loading each component in the actor
                for componentDescriptor in actorDescriptor["components"]:
                    component = Component.loadFromDict(componentDescriptor)
                    actor.addComponent(component)

                scene.actors.append(actor)

            # Returning the whole loaded scene
            return scene

    @staticmethod
    def loadSceneFromFile(fileName):
        with open(fileName, "r") as f:
            try:
                # this is a dictionary
                sceneDescriptor = json.load(f)

                scene = Scene()
                windowDescriptor = sceneDescriptor["window"]
                scene.windowRect.height = windowDescriptor["height"]
                scene.windowRect.width = windowDescriptor["width"]

                for actorDescriptor in sceneDescriptor["actors"]:
                    actor = Actor()
                    actor.name = actorDescriptor["name"]
                    actor.x = actorDescriptor["x"]
                    actor.y = actorDescriptor["y"]

                    for componentDescriptor in actorDescriptor["components"]:
                        component = None
                        if (
                            componentDescriptor["type"]
                            == StaticSpriteComponent.__name__
                        ):
                            component = StaticSpriteComponent(
                                componentDescriptor["fileName"]
                            )
                        elif (
                            componentDescriptor["type"]
                            == BouncingMovementComponent.__name__
                        ):
                            rectDescriptor = componentDescriptor["boundingRect"]
                            r = rect.Rect(
                                rectDescriptor["x"],
                                rectDescriptor["y"],
                                rectDescriptor["width"],
                                rectDescriptor["height"],
                            )
                            component = BouncingMovementComponent(r)
                        else:
                            raise Exception(
                                f"Wrong component type: {componentDescriptor['type']}"
                            )

                        actor.addComponent(component)

                    scene.actors.append(actor)
                return scene

            except Exception as e:
                print(f"Error on filename : {fileName}")
                print(str(e))
