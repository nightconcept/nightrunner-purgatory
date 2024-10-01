# ===============================================================================
# game/event_handlers.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

from typing import Optional, Union

import exceptions
import pygame
import tcod

import game.actions
from game.engine import Engine

from actions import Action, MoveAction, EscapeAction

from keyboard_layout import MOVE_KEYS

ActionOrHandler = Union["game.actions.Action", "EventHandler"]
"""An event handler return value which can trigger an action or switch active handlers.

If a handler is returned then it will become the active handler for future events.
If an action is returned it will be attempted and if it's valid then
MainGameEventHandler will become the active handler.
"""

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
            if keys_pressed in MOVE_KEYS:
                dir = MOVE_KEYS[event.key]
                action = MoveAction(*dir)
                
        return action

    def ev_quit(self, event: pygame.Event) -> Optional[Action]:
        raise SystemExit(0)
    
    def ev_keydown(self) -> Optional[Action]:
        action: Optional[Action] = None
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed in MOVE_KEYS:
            dx, dy = MOVE_KEYS[keys_pressed]
            action = MoveAction(dx=dx, dy=dy)
        elif keys_pressed == tcod.event.K_ESCAPE:
            action = EscapeAction()

        return action