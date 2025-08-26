from objects.base import Object
from utils import load_sprite_sheets
import pygame

class Fruit(Object):
    ANIMATION_DELAY = 3

    def __init__(self, x, y, width, height, fruit_name):
        super().__init__(x, y, width, height, "fruit")
        self.fruit_name = fruit_name
        self.sprites = load_sprite_sheets("Items", "Fruits", "", width, height)
        self.image = self.sprites[self.fruit_name][0]
        self.mask = pygame.mask.from_surface(self.image)
        self.animation_count = 0
        self.animation_name = fruit_name

    def loop(self):
        sprites = self.sprites[self.animation_name]
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.image = sprites[sprite_index]
        self.animation_count += 1
        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.image)
        if self.animation_count // self.ANIMATION_DELAY > len(sprites):
            self.animation_count = 0
