# ===============================================================================
# game/engine.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

from typing import Set, Iterable, Any
from game.entity import Entity
from game.game_map import GameMap
from game.window import Window
from event_handlers import *

# ===============================================================================
# Classes
# ===============================================================================
class Engine:
    """
    Engine class that holds all relevant data together
    """
    def __init__(self, window: Window, entities: Set[Entity], game_map: GameMap):
        self.window =  window
        self.entities = entities
        self.event_handler = MainGameEventHandler(self)
        self.game_map = game_map

    def handle_events(self, event: pygame.Event) -> bool:
        """Handle an event, perform any actions, then return the next active event handler."""
        action_performed = False
        action = self.retrieve_action(event)
        if action is None:
            return False
        try:
            action_performed = action.perform()
        except exceptions.Impossible as ex:
            return False
        return action_performed
    
    def retrieve_action(self, event: pygame.Event) -> Optional[Action]:
        """Return actions from events."""
        response = None
        match event:
            case pygame.KEYDOWN:
                response = self.event_handler.ev_keydown()
        return response

    def render(self) -> bool:
        """Render all entities, map, and UI on screen."""
        self.window.fill(CONFIG.Colors["black"])
        self.game_map.render()
        for entity in self.entities:
            entity.render()
        pygame.display.flip()
