#!/usr/bin/python3
import pygame as pg

import game.float_rect

pg.init()

import sys
from game.background_loop import BackgroundLoop
from settings.settings_handler import get_game_settings
from game import helpers

window_size = helpers.get_screen_dimensions()
screen = pg.display.set_mode(window_size)
pg.display.set_caption("py-planes")

from game.planes.user_plane import UserPlane
from game.planes.enemy_plane import EnemyPlane
from game.planes.control_enemies import EnemyController
from game.planes.enemy_tower import Tower
from game.float_rect import float_rects_collide
from bar import Bar

sys.path.append(r'..')

user_settings = get_game_settings()

fps = int(user_settings.get("fps"))

user_plane_image = pg.image.load('../images/user_plane_images/user_plane_1.png').convert_alpha() # TODO: image must come from json
user_plane = UserPlane(user_plane_image, health=100, armor=100, damage=20) # TODO: hardcoded values must come from json
user_plane.set_spawn_point(
    helpers.calculate_center(window_size[0], user_plane.model.get_width()),
    650
    )

background = BackgroundLoop(fps)
clock = pg.time.Clock()

SPAWN_ENEMY_PLANE = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_ENEMY_PLANE, 5_000)

SPAWN_TOWER = pg.USEREVENT + 2
pg.time.set_timer(SPAWN_TOWER, 8_000)

enemy_planes_surface_objects = [
    pg.image.load(f"../images/enemy_plane_images/enemy_plane_{i}.png").convert_alpha() for i in range(1, 4)
]
tower_img = pg.image.load("../images/buildings/tower_1.png").convert_alpha()

enemies = EnemyController()

health_bar = Bar(500, 760, 145, 25, 100, (21, 43, 79), (110, 137, 181))  # last two tuples are rgb colour codes
armour_bar = Bar(740, 760, 145, 25, 100, (21, 43, 79), (110, 137, 181))  # last two tuples are rgb colour codes


def collision():
    for enemy in enemies.enemy_planes:
        for bullet in enemy.bullets:
            if float_rects_collide(bullet.float_rect, user_plane.float_rect):
                bullet_mask = bullet.bullet_mask
                user_plane_mask = user_plane.plane_mask

                if user_plane_mask.overlap(bullet_mask,
                                           (int(bullet.float_rect.x) - int(user_plane.float_rect.x), int(bullet.float_rect.y) - int(user_plane.float_rect.y))):
                    print(2)
                    return True


running = True
while running:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == SPAWN_ENEMY_PLANE:
            random_image = helpers.get_random_image_of_enemy_planes(enemy_planes_surface_objects)
            enemies.add_enemy(EnemyPlane(random_image, 100, 100, 20))  # TODO: hardcoded values must come from json

        elif event.type == SPAWN_TOWER:
            enemies.add_enemy(Tower(tower_img, 100, 100, 20)) # TODO: hardcoded values must come from json

    background.loop_background(screen)

    keys_pressed = pg.key.get_pressed()

    # if keys_pressed[pg.K_1]:
    #     health_bar.reduce_bar(1)

    #
    # if keys_pressed[pg.K_2]:
    #     armour_bar.reduce_bar(1)


    enemies.update_planes(screen)
    enemies.update_towers(screen, user_plane)

    user_plane.functionality()
    user_plane.display_plane(screen)
    user_plane.update_shot_bullets(screen)

    if collision():
        health_bar.reduce_bar(1)

    armour_bar.draw_bar(screen)
    health_bar.draw_bar(screen)

    pg.display.flip()

pg.quit()
