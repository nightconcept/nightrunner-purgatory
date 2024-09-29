# ===============================================================================
# tiles.py
# reference1: https://pygame.readthedocs.io/en/latest/tiles/tiles.html
# reference2: https://www.youtube.com/watch?v=fGSOHM4mv40
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from typing import Tuple, List
import pygame

# ===============================================================================
# Constants and configuration
# ===============================================================================
DFLT_WIDTH = 16
DFLT_HEIGHT = 16
DFLT_MARGIN = 0
DFLT_SPACE = 0

# ===============================================================================
# Classes
# ===============================================================================
class Tileset:
    def __init__(self, file_path: str, size: Tuple[int, int] = (DFLT_WIDTH, DFLT_HEIGHT), 
                 margin: int = DFLT_MARGIN, spacing: int = DFLT_SPACE):
        """
        Tileset object used to hold tiles loaded from a tilesheet
        :param file_path: Path to tilesheet
        :param size: Tuple of tile size (x, y)
        :param margin: Margin around image in pixels
        :param spacing: Pixels between each tile
        """
        self._tile_table = []
        self._file_path = file_path
        self._size = size
        self._margin = margin
        self._spacing = spacing
        self._image = pygame.image.load(file_path)
        self._rect = self._image.get_rect()
        self.load()

    def load(self):
        """
        Load tilesheet into a tile table
        """
        self.tile_table = []
        x0 = y0 = self._margin
        w, h = self._rect.size
        dx = self._size[0] + self._spacing
        dy = self._size[1] + self._spacing
        
        for x in range(x0, w, dx):
            line = []
            for y in range(y0, h, dy):
                tile = pygame.Surface(self._size)
                tile.blit(self._image, (0, 0), (x, y, *self._size))
                line.append(tile)
            self._tile_table.append(line)

    def get_tile(self, x: int, y: int) -> pygame.Rect:
        """
        Get rect of associated tile
        """
        return self._tile_table[x][y]

    def __str__(self):
        return f'{self.__class__.__name__} file:{self._file_path} tile:{self._size}'