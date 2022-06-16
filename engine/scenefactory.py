import json
from engine.scene import *
from engine.component import *
from engine.actor import *
from engine.staticspritecomponent import *
from engine.bouncingmovementcomponent import *
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
                
                for actorDescriptor in sceneDescriptor["actors"]:
                    actor = Actor()
                    actor.name = actorDescriptor["name"]
                    actor.x = actorDescriptor["x"]
                    actor.y = actorDescriptor["y"]
                    
                    for componentDescriptor in actorDescriptor["components"]:
                        component = None
                        if componentDescriptor["type"] == StaticSpriteComponent.__name__:
                            component = StaticSpriteComponent(componentDescriptor["fileName"])
                        elif componentDescriptor["type"] == BouncingMovementComponent.__name__:
                            rectDescriptor = componentDescriptor["boundingRect"]
                            r = rect.Rect(rectDescriptor["x"], rectDescriptor["y"],
                                rectDescriptor["width"], rectDescriptor["height"])
                            component = BouncingMovementComponent(r)
                        else:
                            raise Exception(f"Wrong component type: {componentDescriptor['type']}")
                        
                        actor.addComponent(component)
                    
                    scene.actors.append(actor)
                return scene
                
            except Exception as e:
                print(f"Error on filename : {fileName}")
                print(str(e))

    def saveSceneToFile(scene, fileName):
        with open(fileName, "w") as f:
            try:
                dict = {}
                windowDict = {}
                windowRect = scene.windowRect
                windowDict["width"] = windowRect.width
                windowDict["height"] = windowRect.height
                dict["window"] = windowDict

                actorsDict = []
                dict["actors"] = actorsDict

                #loop for actors
                for actor in scene.actors:
                   actorDict = {}
                   actorDict["name"] = actor.name
                   actorDict["x"] = actor.x
                   actorDict["y"] = actor.y
                   actorDict["components"] = []
                   
                   #loop for components
                   for component in actor.components:
                      componentDict = {}
                      componentDict["name"] = ""

                      if isinstance(component, StaticSpriteComponent):
                         componentDict["type"] = StaticSpriteComponent.__name__
                         componentDict["fileName"] = component.assetFileName

                      if isinstance(component, BouncingMovementComponent):
                         componentDict["type"] =BouncingMovementComponent.__name__

                         if component.boundingRect is not None:
                            componentDict["boundingRect"] = {}
                            componentDict["boundingRect"]["x"] = component.boundingRect.x
                            componentDict["boundingRect"]["y"] = component.boundingRect.y
                            componentDict["boundingRect"]["width"] = component.boundingRect.width
                            componentDict["boundingRect"]["height"] = component.boundingRect.height
                            
                         componentDict["vx"] = component.vx
                         componentDict["vy"] = component.vy
                         
                      actorDict["components"].append(componentDict)

                   actorsDict.append(actorDict)     

                json.dump(dict, f, indent = 6)
                f.close()

            except Exception as e:
                print(f"Error on filename : {fileName}")
                print(str(e))