# ===============================================================================
# game/game_map.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations
from game.config import Config as CONFIG
from game.tile_types import Tiles as TILES
import numpy as np
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.engine import Engine
    from game.tiles import Tileset

# ===============================================================================
# Classes
# ===============================================================================
class GameMap:
    _engine: Engine
    _initialized: bool
    def __init__(self, width: int, height: int, tileset: Tileset):
        """
        GameMap class which holds all objects in a game map
        :param width: Width of map in units
        :param height: Height of map in units
        """
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=TILES.types["wall"], order="F")

        self.tileset = tileset
        self._initialized = False

    def set_engine(self, engine: Engine) -> None:
        """
        Set engine that map will render to.

        :params engine: Engine the map will render to.
        """
        self._engine = engine
        self._initialized = True

    def in_bounds(self, x: int, y: int) -> bool:
        """
        Return True if x and y are inside of the bounds of this map.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self) -> bool:
        """
        Render the map's tiles to the engine.
        """
        if not self._validate():
            return False
        
        window = self._engine.window.get()

        inner_surface = pygame.Surface((CONFIG.Game["map_width"]*CONFIG.TILE_SIZE,
                                        CONFIG.Game["map_height"]*CONFIG.TILE_SIZE)).convert_alpha()

        inner_surface.fill(CONFIG.Colors["empty"])

        wall_sprite_data: pygame.Surface = self.tileset.get_tile(3, 0)
        floor_sprite_data: pygame.Surface = self.tileset.get_tile(0, 0)

        for y in range(self.height):
            for x in range(self.width):
                tile = self.tiles[x][y]
                draw_tile = None
                if tile == TILES.types["wall"]:
                    draw_tile = wall_sprite_data
                else:
                    draw_tile = floor_sprite_data
                    
                self.draw_tile(x, y, draw_tile, CONFIG.TILE_SIZE)

        window.blit(inner_surface)
        return True

    def draw_tile(self, x: int , y: int, tile: pygame.Surface, tile_size: int):
        """
        Draws an individual tile on the window.
        
        :params x: x-axis coordinate (in tiles) to draw at.
        :params y: y-axis coordinate (in tiles) to draw at.
        :params tile: Surface to draw onto the Window.
        :params tile_size: Size of the tiles drawn in pixels.
        """
        window = self._engine.window.get()
        _x = x * tile_size
        _y = y * tile_size
        window.blit(tile, (_x, _y))

    def _validate(self):
        """
        Helper function that returns whether the GameMap class is ready to use after init(). Expand
        upon this as more requirements are needed.
        """
        return self._initialized