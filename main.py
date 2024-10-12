#!/usr/bin/env python3
# ===============================================================================
# main.py
# main game entrypoint
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from __future__ import annotations
from game.config import Config as CONFIG
from game.engine import Engine
from game.entity import Player, Npc, Entity
from game.game_map import GameMap
from game.procgen import generate_dungeon
from game.tiles import Tileset
from game.window import Window
import pygame
from typing import Set, Tuple

# ===============================================================================
# Constants and configuration
# ===============================================================================

# ===============================================================================
# Local functions
# ===============================================================================
def main() -> None:
    pygame.init()

    window = Window("Yet Another Roguelike Tutorial")
    tileset = Tileset("data/dejavu16x16_gs_tc.png", (16,16), 0, 0)

    player = Player(CONFIG.WINDOW_UNIT_WIDTH // 2, CONFIG.WINDOW_UNIT_HEIGHT // 2, tileset.get_tile(0, 1), "@", CONFIG.Colors["white"])
    npc = Npc(CONFIG.WINDOW_UNIT_WIDTH // 4, CONFIG.WINDOW_UNIT_WIDTH // 2, tileset.get_tile(0, 1), "@", CONFIG.Colors["yellow"])
    entities = [player, npc]

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=CONFIG.WINDOW_UNIT_WIDTH,
        map_height=CONFIG.WINDOW_UNIT_HEIGHT,
        player=player
    )

    engine = Engine(window, entities, game_map, player)

    game_map.set_engine(engine)
    player.set_engine(engine)
    npc.set_engine(engine)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(CONFIG.FPS)
        for event in pygame.event.get(pump=True):
            handled = engine.event_handler.handle_events(event)
            if event.type == pygame.QUIT:
                run = False
        rendered = engine.render()
    pygame.quit()

if __name__ == "__main__":
    main()
