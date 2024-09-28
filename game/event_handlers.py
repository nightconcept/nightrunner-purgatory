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
import game.rendering

from actions import Action

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

    def handle_events(self, event: pygame.Event) -> bool:
        """Handle an event, perform any actions, then return the next active event handler."""
        action_performed = False
        events = pygame.event.get(pump=True)
        for event in events:
            action = self.process_event(event)
            if action is None:
                continue
            try:
                action_performed = action.perform()
            except exceptions.Impossible as ex:
                return False
        return action_performed
    
    def process_event(self, event: pygame.Event) -> Optional[Action]:
        """Return actions from events."""
        response = None
        #TODO
        #if event.type == pygame.KEYDOWN:

    #TODO
    def ev_quit(self, event: pygame.Event) -> Optional[ActionOrHandler]:
        raise SystemExit(0)
    #TODO
    def ev_keydown(self, event: pygame.Event) -> Optional[ActionOrHandler]:
        key = event.sym

        if key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            return game.actions.Move(self.engine.player, dx=dx, dy=dy)
        elif key == tcod.event.K_ESCAPE:
            raise SystemExit(0)

        return None

    def on_render(self, window: pygame.Window) -> None:
        game.rendering.render_map(window, self.engine.game_map)