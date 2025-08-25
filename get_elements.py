import pygame
from settings import WORLD_WIDTH, WORLD_HEIGHT, WIDTH, HEIGHT, FPS, PLAYER_VELOCITY
from player import Player
from objects.block import Block
from objects.fire import Fire

block_size = 96

def get_player():
    #spawn_x = (WORLD_WIDTH // 2) * block_size
    #spawn_y = (WORLD_HEIGHT - 2) * block_size 
    player = Player(100, 100, 50, 50)

    return player

def get_fire_traps():
    fire = Fire(10 * block_size, (WORLD_HEIGHT - 2) * block_size, 16, 32)
    fire.on()

    return fire

def get_blocks():
    objects = []

    # rama de blocuri
    for x in range(WORLD_WIDTH):
        objects.append(Block(x * block_size, 0, block_size)) #up
        objects.append(Block(x * block_size, (WORLD_HEIGHT - 1) * block_size, block_size)) #down

    for y in range(WORLD_HEIGHT):
        objects.append(Block(0, y * block_size, block_size)) #left
        objects.append(Block((WORLD_WIDTH - 1) * block_size, y * block_size, block_size)) #right

    return objects