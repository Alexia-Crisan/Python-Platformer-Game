import pygame
from settings import WIDTH, HEIGHT, FPS, PLAYER_VELOCITY
from game import run_game

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

if __name__ == "__main__":
    run_game(window)
