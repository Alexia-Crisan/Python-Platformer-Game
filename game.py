import pygame
from settings import WIDTH, HEIGHT, FPS, PLAYER_VELOCITY
from utils import get_background
from player import Player
from objects.block import Block
from objects.fire import Fire

def draw(window, background, bg_image, player, objects, offset_x, offset_y):
    window.fill((0, 0, 0))  
    
    for tile in background:
        window.blit(bg_image, (tile[0] - offset_x, tile[1] - offset_y))

    for obj in objects:
        obj.draw(window, offset_x, offset_y)

    player.draw(window, offset_x, offset_y)
    pygame.display.update()

def handle_vertical_collision(player, objects, dy):
    collided_objects = []

    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()
            collided_objects.append(obj)

    return collided_objects

def collide(player, objects, dx):
    player.move(dx, 0)
    player.update()
    collided_objects = None

    for obj in objects:
        if pygame.sprite.collide_mask(player, obj):
            collided_objects = obj
            break

    player.move(-dx, 0)
    player.update()
    return collided_objects

def handle_move(player, objects):
    keys = pygame.key.get_pressed()
    player.x_vel = 0

    collide_left = collide(player, objects, -PLAYER_VELOCITY * 2)
    collide_right = collide(player, objects, PLAYER_VELOCITY * 2)

    if keys[pygame.K_LEFT] and not collide_left:
        player.move_left(PLAYER_VELOCITY)
    if keys[pygame.K_RIGHT] and not collide_right:
        player.move_right(PLAYER_VELOCITY)

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [collide_left, collide_right, *vertical_collide]

    for obj in to_check:
        if obj and obj.name == "fire":
            player.make_hit()

def run_game(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Green.png", WIDTH, HEIGHT)

    block_size = 96
    player = Player(100, 100, 50, 50)
    fire = Fire(100, HEIGHT - block_size - 64, 16, 32)
    fire.on()

    floor = [
        Block(i * block_size, HEIGHT - block_size, block_size)
        for i in range(-WIDTH // block_size, WIDTH * 2 // block_size)
    ]

    objects = [
        *floor,
        Block(0, HEIGHT - block_size * 2, block_size),
        Block(block_size * 3, HEIGHT - block_size * 4, block_size),
        fire,
    ]

    offset_x = 0
    offset_y = 0
    scroll_area_width = 200
    scroll_area_height = 200 

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player.jump_count < 2 and not player.hit:
                    player.jump()

        player.loop(FPS)
        fire.loop()
        handle_move(player, objects)
        draw(window, background, bg_image, player, objects, offset_x, offset_y)

        # horizontal scroll
        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width and player.x_vel > 0) or
           (player.rect.left - offset_x <= scroll_area_width and player.x_vel < 0)):
            offset_x += player.x_vel

        # vertical scroll
        if ((player.rect.bottom - offset_y >= HEIGHT - scroll_area_height and player.y_vel > 0) or
           (player.rect.top - offset_y <= scroll_area_height and player.y_vel < 0)):
            offset_y += player.y_vel

    pygame.quit()
    quit()

