import pygame
from settings import WORLD_WIDTH, WORLD_HEIGHT, WIDTH, HEIGHT, FPS, PLAYER_VELOCITY
from player import Player
from objects.block import Block
from objects.fire import Fire
from objects.trophy import Trophy
from objects.fruits import Fruit

block_size = 96

def get_player():
    spawn_x = 3 * block_size + (block_size - 50) // 2
    spawn_y = 6 * block_size + (block_size - 50) // 2
    player = Player(spawn_x, spawn_y, 50, 50)

    return player

def get_trophy():
    trophy_width, trophy_height = 64, 64
    x, y = 24, 12

    trophy_x = x * block_size - 16
    trophy_y = y * block_size + trophy_height 
    
    trophy = Trophy(trophy_x, trophy_y, trophy_width, trophy_height)

    return trophy

def get_fruits():
    fruit_width, fruit_height = 32, 32
    
    apple_x = (4 - 1) * block_size + 13
    apple_y = (11 - 1) * block_size + fruit_height 

    apple = Fruit(apple_x, apple_y, fruit_width, fruit_height, "Apple")

    banana_x = (9 - 1) * block_size + 13
    banana_y = (24 - 1) * block_size + fruit_height 
    banana = Fruit(banana_x, banana_y, fruit_width, fruit_height, "Bananas")

    cherry_x = (28 - 1) * block_size + 13
    cherry_y = (16 - 1) * block_size + fruit_height 
    cherry = Fruit(cherry_x, cherry_y, fruit_width, fruit_height, "Cherries")

    kiwi_x = (26 - 1) * block_size + 13
    kiwi_y = (6 - 1) * block_size + fruit_height 
    kiwi = Fruit(kiwi_x, kiwi_y, fruit_width, fruit_height, "Kiwi")

    melon_x = (20 - 1) * block_size + 13
    melon_y = (2 - 1) * block_size + fruit_height 
    melon = Fruit(melon_x, melon_y, fruit_width, fruit_height, "Melon")

    orange_x = (40 - 1) * block_size + 13
    orange_y = (2 - 1) * block_size + fruit_height 
    orange = Fruit(orange_x, orange_y, fruit_width, fruit_height, "Orange")

    pineapple_x = (44 - 1) * block_size + 13
    pineapple_y = (3 - 1) * block_size + fruit_height 
    pineapple = Fruit(pineapple_x, pineapple_y, fruit_width, fruit_height, "Pineapple")

    strawberry_x = (43 - 1) * block_size + 13
    strawberry_y = (25 - 1) * block_size + fruit_height 
    strawberry = Fruit(strawberry_x, strawberry_y, fruit_width, fruit_height, "Strawberry")

    return [apple, banana, cherry, kiwi, melon, orange, pineapple, strawberry]

def get_fire_traps():
    fire_coords = [(2, 9), (8, 22), (12, 27), (14, 27), (22, 27), (24, 27), 
                   (26, 27), (35, 27), (47, 27), (48, 27), (35, 27), 
                   (19, 20), (31, 20), (10, 14), (14, 11), (31, 10), (24, 6), 
                   (25, 5), (31, 6), (40, 9), (43, 3), (16, 3), (2, 6)]

    fires = []
    for (x, y) in fire_coords:
        fire_width, fire_height = 16, 32

        fire_x = (x - 1) * block_size + (block_size - fire_width - 16) // 2
        fire_y = (y - 1) * block_size + fire_height 

        fire = Fire(fire_x, fire_y, fire_width, fire_height)
        fire.on()
        fires.append(fire)

    return fires

def get_blocks():
    objects = []

    level_map = [
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,1,1],
        [1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1],
        [1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1],
        [1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,1,1,1,1,1],
        [1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1],
        [1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1,1,0,0,0,1],
        [1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1],
        [1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1],
        [1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,0,1],
        [1,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,0,1,1,0,0,1,0,0,0,1],
        [1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1],
        [1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1],
        [1,0,0,1,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,1],
        [1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1],
        [1,1,0,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0,1],
        [1,0,0,0,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
        [1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,0,1],
        [1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,0,1,0,1,1,1,0,0,0,1],
        [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

    for y, row in enumerate(level_map):
        for x, cell in enumerate(row):
            if cell == 1:
                objects.append(Block(x * block_size, y * block_size, block_size))

    return objects
