#!/usr/bin/env python3
# ===============================================================================
# main.py
# main game entrypoint
# ===============================================================================

# ===============================================================================
# Imports
# ===============================================================================
from game.config import Config as CONFIG
from game.engine import Engine
from game.entity import Player, Npc, Entity
from game.game_map import GameMap
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
    game_map = GameMap(CONFIG.WINDOW_UNIT_WIDTH, CONFIG.WINDOW_UNIT_HEIGHT)
    tileset = Tileset("data/dejavu16x16_gs_tc.png", (16,16), 0, 0)
    player = Entity(CONFIG.WINDOW_WIDTH // 2, CONFIG.WINDOW_HEIGHT // 2, tileset.get_tile(0, 1), "@", CONFIG.Colors["white"])
    npc = Npc(CONFIG.WINDOW_WIDTH // 4, CONFIG.WINDOW_HEIGHT // 2, tileset.get_tile(0, 1), "@", CONFIG.Colors["yellow"])
    entities = set([player, npc])

    engine = Engine(window, entities, game_map, player)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(CONFIG.FPS)
        for event in pygame.event.get(pump=True):
            # using event_handlers.py handle_events() for part2
            handled = engine.event_handler.handle_events(event)
            if event.type == pygame.QUIT:
                run = False
        rendered = engine.render()
    pygame.quit()

if __name__ == "__main__":
    main()
