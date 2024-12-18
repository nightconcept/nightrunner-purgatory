# ===============================================================================
# game/exceptions.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations

# ===============================================================================
# Constants and configuration
# ===============================================================================

# ===============================================================================
# Classes
# ===============================================================================
class Impossible(Exception):
    """Exception raised when an actian is impossible to be performed.
    Reason is in the error message
    """
