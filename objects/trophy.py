from objects.base import Object
from utils import load_sprite_sheets
import pygame

class Trophy(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height, "end")
        self.trophy = load_sprite_sheets("Items", "Checkpoints", "End", width, height)
        self.image = self.trophy["End (Idle)"][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = "End (Idle)"

    def on(self):
        self.animation_name = "End (Pressed) (64x64)"

    def off(self):
        self.animation_name = "End (Idle)"

    def loop(self):
        sprites = self.trophy[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
