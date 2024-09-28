# ===============================================================================
# game/config.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================

class Config:
    Colors = {
        "white": (255, 255, 255),
        "black": (0, 0, 0)
    }

    FPS = 60
    UNIT_SIZE = 16 # in pixels
    WINDOW_UNIT_WIDTH = 80
    WINDOW_UNIT_HEIGHT = 50
    WINDOW_WIDTH = UNIT_SIZE * WINDOW_UNIT_WIDTH
    WINDOW_HEIGHT = UNIT_SIZE * WINDOW_UNIT_HEIGHT
    TEXT_ANTIALIAS_TRUE = 1