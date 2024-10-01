# ===============================================================================
# game/game_map.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

import numpy as np

from game.engine import Engine
from game.tile_types import Tiles as TILES

# ===============================================================================
# Classes
# ===============================================================================
class GameMap:
    engine: Engine
    def __init__(self, width: int, height: int):
        """
        GameMap class which holds all objects in a game map
        :param width: Width of map in units
        :param height: Height of map in units
        """
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=TILES.types["floor"], order="F")

        self.tiles[30:33, 22] = TILES.types["wall"]

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, engine: Engine) -> None:
        #TODO fixup before part 3
        #console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
        return None