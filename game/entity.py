# ===============================================================================
# game/entity.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations
from game.config import Config as CONFIG
import pygame
from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from game.engine import Engine
    from game.entity import Entity

# ===============================================================================
# Classes
# ===============================================================================
class Entity:
    _engine: Engine
    def __init__(
        self,
        x: int,
        y: int,
        image: pygame.Surface,
        char: str,
        color: Tuple[int, int, int],
    ):
        """
        A generic object to represent players, enemies, items, etc.
        :param gamemap: GameMap that the entity will belong to
        :param x: Initial x-coordinate of entity
        :param y: Initial y-coordinate of entity
        :param image: pygame.Surface that is the image of entity
        :param char: Character representing entity
        :param color: Color tuple (r,g,b) of entity
        """
        self.x = x
        self.y = y
        self.image = image
        self.char = char
        self.color = color

    def set_engine(self, engine: Engine) -> None:
        """
        Set engine that entity will render to
        """
        self._engine = engine

    def render(self) -> bool:
        """
        Render this entity onscreen.

        This method must be overridden by Entity subclasses.
        """
        raise NotImplementedError()

    def _validate(self) -> bool:
        """
        Validate that all fields are properly set.

        This method needs _validate_helper() to be overriden by Entity subclasses.
        """
        return isinstance(self._engine, Engine) and self._validate_helper()

    def _validate_helper(self) -> bool:
        """
        Additional validation that must be done to run.

        This method must be overridden by Entity subclasses.
        """
        raise NotImplementedError()   


#TODO eventually merge in to entity of some sort
class Player(Entity):
    """Player class"""
    def __init__(
            self,
            x: int,
            y: int,
            image: pygame.Surface,
            char: str,
            color: Tuple[int, int, int],
        ):
        super().__init__(x, y, image, char, color)
        self.surface = image.subsurface((0, 0, 16, 16))
    
    def render(self):
        pygame.Surface.blit(self._engine.window.get(), self.surface, dest=(self.x * CONFIG.TILE_SIZE, self.y * CONFIG.TILE_SIZE))

    def _validate_helper(self):
        return True

class Npc(Player):
    """NPC class"""
    def __init__(
            self,
            x: int,
            y: int,
            image: pygame.Surface,
            char: str,
            color: Tuple[int, int, int],
        ):
        super().__init__(x, y, image, char, color)
        self.surface = image.subsurface((0, 0, 16, 16))

    def render(self):
        pygame.Surface.blit(self._engine.window.get(), self.surface, dest=(self.x * CONFIG.TILE_SIZE, self.y * CONFIG.TILE_SIZE))

    def _validate_helper(self):
        return True