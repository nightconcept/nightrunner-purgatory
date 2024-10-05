# ===============================================================================
# game/config.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from typing import Tuple

# ===============================================================================
# Classes
# ===============================================================================
class Config:
    """
    Common configuration dictionaries.
    """

    Colors: dict[str, Tuple]= {
        "empty": (0, 0, 0, 0),
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "yellow": (255, 255, 0)
    }
    """
    Common color dictionary values.
    #TODO move to constant file someday?
    """

    Game: dict[str, int] = {
        "map_width": 30,
        "map_height": 30,
        "fps": 60,
        "tile_size": 16
    }
    """
    Game configuration values.
    """

    FPS = 60
    UNIT_SIZE = 16 # in pixels
    TILE_SIZE = 16 # in pixels
    WINDOW_UNIT_WIDTH = 80
    WINDOW_UNIT_HEIGHT = 50
    WINDOW_WIDTH = UNIT_SIZE * WINDOW_UNIT_WIDTH
    WINDOW_HEIGHT = UNIT_SIZE * WINDOW_UNIT_HEIGHT
    TEXT_ANTIALIAS_TRUE = 1