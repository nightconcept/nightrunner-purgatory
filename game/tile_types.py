# ===============================================================================
# game/tile_types.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
import numpy as np  # type: ignore

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("id", np.int32),
        ("walkable", np.bool),
        ("transparent", np.bool),
    ]
)

# ===============================================================================
# Local Functions
# ===============================================================================
def new_tile(*, id: int, walkable: bool, transparent: bool) -> np.ndarray:
    """
    Helper function for generating a new tile.

    :param id: ID number for the tile #TODO Make this actually unique?
    :param walkable: True if this tile can be walked over.
    :param transparent: rue if this tile doesn't block FOV.
    """
    return np.array((id, walkable, transparent), dtype=tile_dt)

# ===============================================================================
# Classes
# ===============================================================================
class Tiles:
    types ={
        "floor": new_tile(id=1, walkable=True, transparent=True),
        "wall": new_tile(id=2, walkable=False, transparent=False)
    }
