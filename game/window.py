# ===============================================================================
# game/window.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from typing import Set, Tuple
import pygame

from game.config import Config as CONFIG
from game.entity import Entity

# ===============================================================================
# Classes
# ===============================================================================
class Window:
    """
    Window class that is the pygame display and tcod console."""
    def __init__(
            self,
            caption: str,
            width: int = CONFIG.WINDOW_WIDTH,
            height: int = CONFIG.WINDOW_HEIGHT,
            unit_width: int = CONFIG.UNIT_SIZE,
            unit_height: int = CONFIG.UNIT_SIZE
        ):
        """
        Define pygame window and tcod console.

        :param x: x-coordinate to draw entity
        :param y: y-coordinate to draw entity
        :param entity: the entity to draw 
        """
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

    def fill(self, color: tuple[int, int, int] | pygame.Color) -> None:
        self.window.fill(color)

    def get_window(self) -> pygame.Surface:
        return self.window
    
    def console_tiles_rgb(self) -> None:
        pass
    
    def console_print(self, x: int, y: int, entity: Entity) -> None:
        """
        Emulates the console.print() function of tcodlib

        :param x: x-coordinate to draw entity
        :param y: y-coordinate to draw entity
        :param entity: the entity to draw 
        """
        pass