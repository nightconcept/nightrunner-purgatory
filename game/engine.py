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
    def __init__(self, window: pygame.Window, entities: Set[Entity], player: Entity, game_map: GameMap):
        self.window =  window
        self.entities = entities
        self.event_handler = MainGameEventHandler(self)
        self.player = player
        self.game_map = game_map

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
        match event:
            case pygame.KEYDOWN:
                response = self.event_handler.ev_keydown()
            
        return response
