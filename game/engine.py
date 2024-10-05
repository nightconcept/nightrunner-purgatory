# ===============================================================================
# game/engine.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

from event_handlers import MainGameEventHandler
import exceptions
from game.actions import Action
from game.entity import Entity, Player
from game.game_map import GameMap
from game.window import Window
from game.config import Config as CONFIG
import pygame

from typing import Optional, Set

# ===============================================================================
# Classes
# ===============================================================================
class Engine:
    """
    Engine class that holds all relevant data together.
    """
    def __init__(self, window: Window, entities: Set[Entity], game_map: GameMap, player: Entity):
        self.window =  window
        for entity in entities:
            entity.set_engine(self)
        self.entities = entities
        self.event_handler = MainGameEventHandler(self)
        self.game_map = game_map
        self.game_map.set_engine(self)
        self.player = player

    def handle_events(self, event: pygame.Event) -> bool:
        """Handle an event, perform any actions, then return the next active event handler."""
        action_performed = False
        action: Action | None = self.retrieve_action(event)
        if action is None:
            return False
        try:
            action_performed = action.perform(self, self.player)
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
        try:
            self.window.fill(CONFIG.Colors["black"])
            self.game_map.render()
            for entity in self.entities:
                entity.render()
            pygame.display.flip()
        except exceptions.Impossible as ex:
            return False
        return True
