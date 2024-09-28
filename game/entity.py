# ===============================================================================
# game/entity.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

from typing import Tuple

import game.game_map

# ===============================================================================
# Classes
# ===============================================================================
class Entity:
    def __init__(
        self,
        gamemap: game.game_map.GameMap,
        x: int,
        y: int,
        char: str,
        color: Tuple[int, int, int],
    ):
        """
        A generic object to represent players, enemies, items, etc.
        :param gamemap: GameMap that the entity will belong to
        :param x: Initial x-coordinate of entity
        :param y: Initial y-coordinate of entity
        :param char: Character representing entity
        :param color: Color tuple (r,g,b) of entity
        """
        self.gamemap = gamemap
        gamemap.entities.add(self)
        self.x = x
        self.y = y
        self.char = char
        self.color = color
