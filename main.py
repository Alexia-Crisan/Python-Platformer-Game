import pygame
from settings import WIDTH, HEIGHT, FPS, PLAYER_VELOCITY
from player import Player
from objects.block import Block
from objects.fire import Fire
from utils import get_background
from game import run_game

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

if __name__ == "__main__":
    run_game(window)
