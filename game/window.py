# ===============================================================================
# game/window.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from typing import Set, Tuple
import pygame

from game.config import Config as CONFIG

# ===============================================================================
# Classes
# ===============================================================================
class Window:
    """Window class that is the pygame display and manages all the items that need to be drawn on screen"""
    def __init__(
            self,
            caption: str,
            width: int =CONFIG.WINDOW_WIDTH,
            height: int =CONFIG.WINDOW_HEIGHT
        ):
        self.win = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

    def fill(self, color: tuple[int, int, int] | pygame.Color):
        self.win.fill(color)

    def get(self):
        return self.win