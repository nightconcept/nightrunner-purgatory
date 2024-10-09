# ===============================================================================
# game/window.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from game.config import Config as CONFIG
import pygame
from typing import Set, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
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
            tile_width: int = CONFIG.UNIT_SIZE,
            tile_height: int = CONFIG.UNIT_SIZE
        ):
        """
        Define pygame window and tcod console.

        :param caption: Title in titlebar of window.
        :param width: Pixel width of window.
        :param height: Pixel height of window.
        :param tile_width: Size in pixels of a unit.
        :param tile_height: Size in pixels of a unit.
        """
        self._window: pygame.Surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)

    def fill(self, color: tuple[int, int, int] | pygame.Color) -> None:
        self._window.fill(color)

    def get(self) -> pygame.Surface:
        """
        Get Window()'s pygame.Surface for rendering.

        :returns: Window()'s pygame.Surface
        """
        return self._window
    
    def console_tiles_rgb(self) -> None:
        pass
    
    def console_print(self, x: int, y: int, entity: Entity) -> None:
        """
        Emulates the console.print() function of tcodlib

        :param x: X-coordinate (unit-scale) to draw entity.
        :param y: X-coordinate (unit-scale) to draw entity.
        :param entity: The entity to draw.
        """
        pass
