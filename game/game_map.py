# ===============================================================================
# game/game_map.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

from typing import Set

import numpy as np

from game.engine import Engine
import game.entity

#TODO REDO PART 2
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
        self.tiles = np.zeros((width, height), dtype=np.uint8, order="F")
        self.entities: Set[game.entity.Entity] = set()

    def set_engine(self, engine: Engine):
        self.engine = engine

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height
    
    def validate(self):
        """
        Validate that all parameters needed to be set are set.
        Return True if GameMap can be used.
        """
        return isinstance(self.engine, Engine)