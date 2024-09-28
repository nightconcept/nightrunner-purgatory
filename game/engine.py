# ===============================================================================
# game/engine.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

import game.entity
import game.game_map

# ===============================================================================
# Classes
# ===============================================================================
class Engine:
    """
    Engine class that holds all relevant data together
    """
    game_map: game.game_map.GameMap
    player: game.entity.Entity
