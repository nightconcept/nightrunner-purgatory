#!/usr/bin/env python3
# ===============================================================================
# main.py
# main game entrypoint
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from typing import Tuple
from tiles import Tileset
import pygame
import tcod

from game.engine import Engine
from game.entity import Entity, Player
from game.game_map import GameMap
import game.event_handlers
from game.window import Window
from game.config import Config as CONFIG


# ===============================================================================
# Inits
# ===============================================================================
pygame.init()

# ===============================================================================
# Constants and configuration
# ===============================================================================

# ===============================================================================
# Local functions
# ===============================================================================
def main() -> None:

    window = Window(CONFIG.WINDOW_WIDTH, CONFIG.WINDOW_HEIGHT, "Yet Another Roguelike Tutorial")
    game_map = GameMap(CONFIG.WINDOW_UNIT_WIDTH, CONFIG.WINDOW_UNIT_HEIGHT)
    tileset = Tileset("data/dejavu16x16_gs_tc.png", (16,16), 0, 0)
    player = Entity(game_map, CONFIG.WINDOW_WIDTH // 2, CONFIG.WINDOW_HEIGHT // 2, tileset.get_tile(0, 1), "@", CONFIG.Colors["white"])
    npc = Entity(game_map, CONFIG.WINDOW_WIDTH // 4, CONFIG.WINDOW_HEIGHT // 2, tileset.get_tile(0, 1), "@", CONFIG.Colors["yellow"])
    entities = set([player, npc])

    engine = Engine(window, entities, player, game_map)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(CONFIG.FPS)
        for event in pygame.event.get(pump=True):
            handled = engine.event_handler.handle_events(event)
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


if __name__ == "__main__":
    main()
