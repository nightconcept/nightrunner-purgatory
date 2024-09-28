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

import game.engine
import game.entity
import game.game_map
import game.event_handlers


# ===============================================================================
# Inits
# ===============================================================================
pygame.init()

# ===============================================================================
# Constants and configuration
# ===============================================================================
## Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

## Controls
P1_CONTROL_UP = pygame.K_w
P1_CONTROL_DOWN = pygame.K_s
P1_CONTROL_LEFT = pygame.K_a
P1_CONTROL_RIGHT = pygame.K_d

## Screen and settings
FPS = 60
VOLUME = 0.3
UNIT_SIZE = 16 # in pixels
WINDOW_UNIT_WIDTH = 80
WINDOW_UNIT_HEIGHT = 50
WINDOW_WIDTH = UNIT_SIZE * WINDOW_UNIT_WIDTH
WINDOW_HEIGHT = UNIT_SIZE * WINDOW_UNIT_HEIGHT
TEXT_ANTIALIAS_TRUE = 1

# ===============================================================================
# Classes
# ===============================================================================
class Window:
    """Window class that is the pygame display and manages all the items that need to be drawn on screen"""
    def __init__(self, width, height, caption):
        self.win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.draw_items = []
        pygame.display.set_caption(caption)

    # may become relevant at some point
    def draw(self):
        self.win.fill(BLACK)
        for item in self.draw_items:
            item.draw()
        pygame.display.flip()

    def add_draw_item(self, item):
        self.draw_items.append(item)

    def get_surface(self):
        return self.win

class Player:
    """Player class"""
    def __init__(self, window, x, y, image):
        self.window = window
        self.x = x
        self.y = y

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

    return delta_x * UNIT_SIZE, delta_y * UNIT_SIZE
    

def main() -> None:
    player_x: int = WINDOW_WIDTH // 2
    player_y: int = WINDOW_HEIGHT // 2

    engine = game.engine.Engine()
    engine.game_map = game.game_map.GameMap(engine, WINDOW_UNIT_WIDTH, WINDOW_UNIT_HEIGHT)
    engine.game_map.tiles[1:-1, 1:-1] = 1
    engine.game_map.tiles[30:33, 22] = 0
    engine.player = game.entity.Entity(engine.game_map, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, "@", (255, 255, 255))

    game.entity.Entity(engine.game_map, WINDOW_WIDTH // 2 - 5, WINDOW_HEIGHT // 2, "@", (255, 255, 0))  # NPC

    event_handler = game.event_handlers.MainGameEventHandler(engine)

    tileset = Tileset("data/dejavu16x16_gs_tc.png", (16,16), 0, 0)

    window = Window(WINDOW_WIDTH, WINDOW_HEIGHT, "Yet Another Roguelike Tutorial")
    player = Player(window, player_x, player_y, tileset.get_tile(0, 1))
    window.add_draw_item(player)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            event_handler = event_handler.handle_events(event)

            if event.type == pygame.QUIT:
                run = False

        window.draw()
    pygame.quit()


if __name__ == "__main__":
    main()
