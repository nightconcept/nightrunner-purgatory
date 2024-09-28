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
        self.draw_items = []
        pygame.display.set_caption(caption)

    # may become relevant at some point
    def draw(self):
        self.win.fill(CONFIG.Colors["black"])
        for item in self.draw_items:
            item.draw()
        pygame.display.flip()

    def add_draw_item(self, item):
        self.draw_items.append(item)

    def get_surface(self):
        return self.win