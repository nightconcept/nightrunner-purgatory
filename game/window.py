# ===============================================================================
# game/window.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
import pygame

from game.config import Config as CONFIG

# ===============================================================================
# Classes
# ===============================================================================
class Window:
    """Window class that is the pygame display and manages all the items that need to be drawn on screen"""
    def __init__(self, width, height, caption):
        self.win = pygame.display.set_mode((CONFIG.WINDOW_WIDTH, CONFIG.WINDOW_HEIGHT))
        pygame.display.set_caption(caption)

    def get_surface(self):
        return self.win