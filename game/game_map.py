# ===============================================================================
# game/game_map.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

from typing import Set

import numpy as np

import game.engine
import game.entity

#TODO REDO PART 2
# ===============================================================================
# Classes
# ===============================================================================
class GameMap:
    def __init__(self, engine: game.engine.Engine, width: int, height: int):
        """
        GameMap class which holds all objects in a game map
        :param engine: Engine object to associate with
        :param width: Width of map in units
        :param height: Height of map in units
        """
        self.engine = engine
        self.width, self.height = width, height
        self.tiles = np.zeros((width, height), dtype=np.uint8, order="F")
        self.entities: Set[game.entity.Entity] = set()

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height