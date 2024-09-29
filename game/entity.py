# ===============================================================================
# game/entity.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

from typing import Tuple

from game.engine import Engine
import game.game_map
import pygame

# ===============================================================================
# Classes
# ===============================================================================
class Entity:
    engine: Engine
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

    def render(self) -> bool:
        """
        Draw this entity onscreen.

        This method must be overridden by Entity subclasses.
        """
        raise NotImplementedError()

    def _validate(self) -> bool:
        """
        Validate that all fields are properly set.

        This method must be overridden by Entity subclasses.
        """
        return isinstance(self.engine, Engine) and self._validate_helper()

    def _validate_helper(self) -> bool:
        """
        Additional validation that must be done to run.

        This method must be overridden by Entity subclasses.
        """
        raise NotImplementedError()   


#TODO eventually merge in to entity of some sort
class Player(Entity):
    """Player class"""
    def __init__(self, image: pygame.Rect):
        self.rect = image.subsurface((0, 0, 16, 16))

    def move(self, x, y):
        self.x += x
        self.y += y
    
    def render(self):
        pygame.Surface.blit(self.window.get_surface(), self.rect, dest=(self.x, self.y))