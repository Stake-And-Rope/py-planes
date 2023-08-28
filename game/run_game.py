#!/usr/bin/python3
import pygame as pg

import game.float_rect
from game.extra_bullets_powerup import ExtraBulletsPowerUp
from game.powerup_controller import PowerupController

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
user_plane.create_user_bar(
    bar_type="health_bar", # creates instance attr with that name
    x=500,
    y=760,
    width=145,
    height=25,
    max_value=user_plane.health,
    top_color=(21, 43, 79),
    bottom_color=(110, 137, 181)
    )
user_plane.create_user_bar(
    bar_type="armor_bar", # creates instance attr with that name
    x=740,
    y=760,
    width=145,
    height=25,
    max_value=user_plane.armor,
    top_color=(21, 43, 79),
    bottom_color=(110, 137, 181)
    )

background = BackgroundLoop(fps)
clock = pg.time.Clock()

SPAWN_ENEMY_PLANE = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_ENEMY_PLANE, 5_000)

SPAWN_TOWER = pg.USEREVENT + 2
pg.time.set_timer(SPAWN_TOWER, 8_000)

EXTRA_BULLETS_POWERUP = pg.USEREVENT + 3
pg.time.set_timer(EXTRA_BULLETS_POWERUP, 30_000)

enemy_planes_surface_objects = [
    pg.image.load(f"../images/enemy_plane_images/enemy_plane_{i}.png").convert_alpha() for i in range(1, 4)
]
tower_img = pg.image.load("../images/buildings/tower_1.png").convert_alpha()

enemies = EnemyController()

extra_bullets_powerup = ExtraBulletsPowerUp(image=pg.image.load("../images/power_ups/powerup_x2.png").convert_alpha())
powers_controller = PowerupController()

def collision(curr_enemy):
    not_collided_bullets = []

    for bullet in curr_enemy.bullets:
        if float_rects_collide(bullet.float_rect, user_plane.float_rect):
            bullet_mask = bullet.bullet_mask
            user_plane_mask = user_plane.plane_mask

            if not user_plane_mask.overlap(bullet_mask,
                                       (int(bullet.float_rect.x) - int(user_plane.float_rect.x), int(bullet.float_rect.y) - int(user_plane.float_rect.y))):
                pass
            else:
                not_collided_bullets.append(bullet)
        else:
            not_collided_bullets.append(bullet)


    if len(not_collided_bullets) < len(curr_enemy.bullets):
        len_all_enemy_bullets, len_all_not_collided_bullets = len(curr_enemy.bullets), len(not_collided_bullets)
        curr_enemy.bullets = not_collided_bullets
        return len_all_enemy_bullets - len_all_not_collided_bullets

    return False



running = True
while running:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == SPAWN_TOWER:
            enemies.add_enemy(Tower(tower_img, 100, 100, 20))  # TODO: hardcoded values must come from json

        elif event.type == SPAWN_ENEMY_PLANE:
            random_image = helpers.get_random_image_of_enemy_planes(enemy_planes_surface_objects)
            enemies.add_enemy(EnemyPlane(random_image, 100, 100, 20))  # TODO: hardcoded values must come from json

        elif event.type == EXTRA_BULLETS_POWERUP:
            powers_controller.extra_bullets = extra_bullets_powerup

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

    powers_controller.render_extra_bullets(screen=screen, user_plane=user_plane)

    # if collision():
    #     user_plane.armor_bar.reduce_bar(1)
    #     if user_plane.armor_bar.current_width == 0:
    #         user_plane.health_bar.reduce_bar(1)

    for enemy in enemies.enemy_planes:
        result = collision(enemy)

        if user_plane.armor_bar.current_width == 0:
            user_plane.health_bar.reduce_bar(1 * result)
        else:
            user_plane.armor_bar.reduce_bar(1 * result)

    user_plane.armor_bar.draw_bar(screen)
    user_plane.health_bar.draw_bar(screen)

    pg.display.flip()

pg.quit()
