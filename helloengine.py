import sys
from engine.engine import Engine

# Global state variable
engine = Engine()

engine.loadScene("pathtest.json")

# game loop
engine.gameLoop()

sys.exit()