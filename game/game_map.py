# ===============================================================================
# game/game_map.py
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations



from game.config import Config as CONFIG
from game.engine import Engine
from game.tile_types import Tiles as TILES
import numpy as np
import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine

# ===============================================================================
# Classes
# ===============================================================================
class GameMap:
    _engine: Engine
    def __init__(self, width: int, height: int):
        """
        GameMap class which holds all objects in a game map
        :param width: Width of map in units
        :param height: Height of map in units
        """
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=TILES.types["floor"], order="F")

        self.tiles[30:33, 22] = TILES.types["wall"]

    def set_engine(self, engine: Engine) -> None:
        """
        Set engine that map will render to
        """
        self._engine = engine

    def in_bounds(self, x: int, y: int) -> bool:
        """
        Return True if x and y are inside of the bounds of this map.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self) -> None:
        """
        Return True if x and y are inside of the bounds of this map.

        :params engine: 
        """
        if not self._validate():
            return
        
        window = self._engine.window.get()

        inner_surface = pygame.Surface(
            (CONFIG.Game["map_width"]*CONFIG.TILE_SIZE,
             CONFIG.Game["map_height"]*CONFIG.TILE_SIZE)).convert_alpha()

        inner_surface.fill(CONFIG.Colors["empty"])

        # TODO from here https://github.com/ZachAttakk/RLDev2020/blob/master/render_functions.py#L55
        wall_sprite_data = sprites.get("wall")
        wall_sprite_image = self.spritesheets.get(wall_sprite_data.get(
            "sheet")).sprite_at(wall_sprite_data)

        floor_sprite_data = sprites.get("floor")
        floor_sprite_image = self.spritesheets.get(floor_sprite_data.get(
            "sheet")).sprite_at(floor_sprite_data)

        # now when we render the map and entities, we do so to this inner surface
        # We'll also need to grab the player position when we see it
        player_pos = (window.get_width()//2, window.get_width()//2)

        # render tiles either visible, explored, unexplored
        for y in range(game_map.height):
            for x in range(game_map.width):
                # get tile info for rendering
                tile = game_map.tiles[x][y]
                explored = game_map.explored[x][y]
                visible = game_map.visible[x][y]

                # if it's not explored, we don't show it at all
                if explored:
                    if tile == tile_types.wall:
                        self.draw_tile(inner_surface, x, y,
                                       wall_sprite_image, tile_size)
                    else:
                        self.draw_tile(inner_surface, x, y,
                                       floor_sprite_image, tile_size)
                        pass

                    # if it's not currently in LOS, we draw grey over it.
                    if not visible:
                        darken = pygame.Surface(
                            (tile_size, tile_size)).convert()
                        darken.fill(CONFIG.get_colour("black"))
                        darkness = CONFIG.Display.get("darkness_opacity") or 0
                        darken.set_alpha(darkness)
                        self.draw_tile(inner_surface, x, y, darken, tile_size)

        # Render entities on visible tiles
        entities_sorted_for_rendering = sorted(
            game_map.entities, key=lambda x: x.render_order.value
        )
        for _ent in entities_sorted_for_rendering:
            # only render if visible
            _ent_pos = list(_ent.position)
            if game_map.visible[_ent_pos[0], _ent_pos[1]]:
                # get sprite
                ent_sprite_image = self.spritesheets.get(
                    _ent.sprite.get("sheet")).sprite_at(_ent.sprite)
                self.draw_entity(inner_surface, _ent,
                                 ent_sprite_image, tile_size)
                # if this is the player, grab its position on screen
                if _ent == game_map.engine.PLAYER:
                    player_pos = (_ent_pos[0] * tile_size,
                                  _ent_pos[1]*tile_size)

        # offset map to center player, then blit to window
        # we use width in both cases because the display will remain square as much as possible
        offset = (window.get_width()//2 - player_pos[0],
                  window.get_width()//2 - player_pos[1])

        # check and save map offset
        if offset != self.map_offset:
            self.map_offset_old = self.map_offset
            self.map_offset = offset

        # TODO: Make lerp from one to other

        window.blit(inner_surface, offset)  # that 0,0 is what we need to replace

    
    def _validate(self) -> bool:
        """
        Validate that all fields are properly set.
        """
        return isinstance(self._engine, Engine)