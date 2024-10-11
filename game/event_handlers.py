# ===============================================================================
# game/event_handlers.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations
import game.actions
from game.actions import Action, MoveAction, EscapeAction
from game.keyboard_layout import MOVE_KEYS
import pygame
import tcod
from typing import Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from game.engine import Engine
    from game.entity import Entity

# ===============================================================================
# Classes
# ===============================================================================
class EventHandler:
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self):
        raise NotImplementedError()

class MainGameEventHandler(EventHandler):
    def __init__(self, engine: Engine) -> None:
        super().__init__(engine)

    def handle_events(self, event: pygame.Event) -> Optional[Action]:
        action: Optional[Action] = None
        if event.type == pygame.KEYDOWN:
            keys_pressed = pygame.key.get_pressed()
            move_key = None
            if keys_pressed[pygame.K_UP]:
                move_key = pygame.K_UP
            elif keys_pressed[pygame.K_DOWN]:
                move_key = pygame.K_DOWN
            elif keys_pressed[pygame.K_LEFT]:
                move_key = pygame.K_LEFT
            elif keys_pressed[pygame.K_RIGHT]:
                move_key = pygame.K_RIGHT
            if move_key != None:
                dir = MOVE_KEYS[move_key]
                action = MoveAction(*dir)
                action.perform(self.engine, self.engine.player)
                
        return action
