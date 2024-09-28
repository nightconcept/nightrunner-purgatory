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
from game.entity import Entity
import game.game_map
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

## Controls
P1_CONTROL_UP = pygame.K_w
P1_CONTROL_DOWN = pygame.K_s
P1_CONTROL_LEFT = pygame.K_a
P1_CONTROL_RIGHT = pygame.K_d

## Screen and settings
VOLUME = 0.3


# ===============================================================================
# Classes
# ===============================================================================
class Player:
    """Player class"""
    def __init__(self, window, x, y, image):
        self.window = window
        self.x = x
        self.y = y
        self.rect = image.subsurface((0, 0, 16, 16))

    def move(self, x, y):
        self.x += x
        self.y += y
    
    def draw(self):
        pygame.Surface.blit(self.window.get_surface(), self.rect, dest=(self.x, self.y))

# ===============================================================================
# Local functions
# ===============================================================================
def get_movement(keys_pressed) -> Tuple[int, int]:
    #TODO add debouncing since diagonal movement is 2x movement speed
    delta_x = 0
    delta_y = 0
    if keys_pressed[P1_CONTROL_LEFT]:
        delta_x = -1
    if keys_pressed[P1_CONTROL_RIGHT]: # UP
        delta_x = 1
    if keys_pressed[P1_CONTROL_UP]: # UP
        delta_y = -1
    if keys_pressed[P1_CONTROL_DOWN]: # UP
        delta_y = 1

    return delta_x * CONFIG.UNIT_SIZE, delta_y * CONFIG.UNIT_SIZE
    

def main() -> None:

    window = Window(CONFIG.WINDOW_WIDTH, CONFIG.WINDOW_HEIGHT, "Yet Another Roguelike Tutorial")
    game_map = GameMap(engine, CONFIG.WINDOW_UNIT_WIDTH, CONFIG.WINDOW_UNIT_HEIGHT)
    tileset = Tileset("data/dejavu16x16_gs_tc.png", (16,16), 0, 0)
    player = Entity(game_map, CONFIG.WINDOW_WIDTH // 2, CONFIG.WINDOW_HEIGHT // 2, tileset.get_tile(0, 1), "@", CONFIG.Colors["white"])

    engine = Engine(window, [], player, game_map)
    

    #TODO
    engine.game_map.tiles[1:-1, 1:-1] = 1
    engine.game_map.tiles[30:33, 22] = 0


    game.entity.Entity(engine.game_map, CONFIG.WINDOW_WIDTH // 2 - 5, CONFIG.WINDOW_HEIGHT // 2, "@", (255, 255, 0))  # NPC

    event_handler = game.event_handlers.MainGameEventHandler(engine)

    #player = Player(window, player_x, player_y, tileset.get_tile(0, 1))

    window.add_draw_item(player)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(CONFIG.FPS)
        for event in pygame.event.get():
            event_handler = event_handler.handle_events(event)

            if event.type == pygame.QUIT:
                run = False

        window.draw()
    pygame.quit()


if __name__ == "__main__":
    main()
