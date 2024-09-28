# ===============================================================================
# game/entity.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

from typing import Tuple

import game.game_map
import pygame

# ===============================================================================
# Classes
# ===============================================================================
class Entity:
    def __init__(
        self,
        gamemap: game.game_map.GameMap,
        x: int,
        y: int,
        image: pygame.Rect,
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
        self.image = image
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        # TODO: Remove later in tutorial as separate tutorial moved this
        # to actions.py
        self.x += dx
        self.y += dy
