# ===============================================================================
# game/actions.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

import game.entity

# ===============================================================================
# Classes
# ===============================================================================
class Action:
    def __init__(self, entity: game.entity.Entity) -> None:
        """
        Action class that can be performed.
        :param entity: Entity which will perform the action
        """
        super().__init__()
        self.entity = entity  # The object performing the action.
        self.engine = entity.gamemap.engine

    def perform(self) -> bool:
        """Perform this action now.

        This method must be overridden by Action subclasses.
        """
        raise NotImplementedError()
    
class Move(Action):
    def __init__(self, entity: game.entity.Entity, dx: int, dy: int):
        """
        Move action will move the associated entity.
        :param entity: Entity which will perform the move.
        """
        super().__init__(entity)

        self.dx = dx
        self.dy = dy

    def perform(self) -> bool:
        dest_x = self.entity.x + self.dx
        dest_y = self.entity.y + self.dy

        if not self.engine.game_map.in_bounds(dest_x, dest_y):
            return False # Destination is out of bounds.
        if not self.engine.game_map.tiles[dest_x, dest_y]:
            return False # Destination is blocked by a tile.

        self.entity.x, self.entity.y = dest_x, dest_y
        return True
