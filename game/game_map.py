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
    from engine import Engine

# ===============================================================================
# Classes
# ===============================================================================
class GameMap:
    _engine: Engine
    def __init__(self, width: int, height: int):
        """
        GameMap class which holds all objects in a game map
        :param width: Width of map in units
        :param height: Height of map in units
        """
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=TILES.types["floor"], order="F")

        self.tiles[30:33, 22] = TILES.types["wall"]

    def set_engine(self, engine: Engine) -> None:
        """
        Set engine that map will render to.

        :params engine: Engine the map will render to.
        """
        self._engine = engine

    def in_bounds(self, x: int, y: int) -> bool:
        """
        Return True if x and y are inside of the bounds of this map.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self) -> None:
        """
        Render the map's tiles to the engine.
        """
        if not self._validate():
            return
        
        window = self._engine.window.get()

        inner_surface = pygame.Surface(
            (CONFIG.Game["map_width"]*CONFIG.TILE_SIZE,
             CONFIG.Game["map_height"]*CONFIG.TILE_SIZE)).convert_alpha()

        inner_surface.fill(CONFIG.Colors["empty"])

        # TODO from here https://github.com/ZachAttakk/RLDev2020/blob/master/render_functions.py#L55
        wall_sprite_data = sprites.get("wall")
        wall_sprite_image = self.spritesheets.get(wall_sprite_data.get(
            "sheet")).sprite_at(wall_sprite_data)

        floor_sprite_data = sprites.get("floor")
        floor_sprite_image = self.spritesheets.get(floor_sprite_data.get(
            "sheet")).sprite_at(floor_sprite_data)

        # render tiles either visible, explored, unexplored
        for y in range(self.height):
            for x in range(self.width):
                # get tile info for rendering
                # TODO, tie together what the tile needs to be with rendering it
                tile = self.tiles[x][y]

                # TODO, this should be whichever image is there
                self.draw_tile(x, y, floor_sprite_image, CONFIG.TILE_SIZE)

        # TODO end
        window.blit(inner_surface)

    def draw_tile(self, x:int , y: int, tile: pygame.Surface, tile_size: int):
        window = self._engine.window.get()
        _x = x * tile_size
        _y = y * tile_size
        window.blit(tile, (_x, _y))
    
    def _validate(self) -> bool:
        """
        Validate that all fields are properly set.
        """
        return isinstance(self._engine, Engine)
