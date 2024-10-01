# ===============================================================================
# game/actions.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity
    
# ===============================================================================
# Classes
# ===============================================================================
class Action:
    def perform(self, engine: Engine, entity: Entity) -> bool:
        """Perform this action with the objects needed to determine its scope.

        `engine` is the scope this action is being performed in.

        `entity` is the object performing the action.

        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()
    
class MoveAction(Action):
    def __init__(self, dx: int, dy: int):
        """
        Move action across a distance.

        :param dx: Distance to move along x-axis.
        :param dy: Distance to move along y-axis.
        """
        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity) -> bool:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return False # Destination is out of bounds.
        if not engine.game_map.tiles[dest_x, dest_y]:
            return False # Destination is blocked by a tile.

        entity.x, entity.y = dest_x, dest_y
        return True

class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity) -> bool:
        raise SystemExit()
        