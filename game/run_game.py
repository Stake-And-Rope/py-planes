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
from game.collision import check_user_plane_collision, check_enemy_collision, check_user_plane_and_enemies_collision

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

collision_with_enemy = False
font_text = pg.font.SysFont('freesansbold.ttf', 35)


def new_window():
    background.loop_background(screen)
    text = font_text.render('You lose!', True, (250, 0, 0))
    screen.blit(text, text.get_rect(center=(450, 400)))


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

    if collision_with_enemy:
        new_window()
        pg.display.flip()
        continue

    background.loop_background(screen)

    keys_pressed = pg.key.get_pressed()

    enemies.update_planes(screen)
    enemies.update_towers(screen, user_plane)

    user_plane.functionality()
    user_plane.display_plane(screen)
    user_plane.update_shot_bullets(screen)

    powers_controller.render_extra_bullets(screen=screen, user_plane=user_plane)

    check_user_plane_collision(enemies, user_plane)
    check_enemy_collision(enemies, user_plane)

    if check_user_plane_and_enemies_collision(enemies, user_plane):
        collision_with_enemy = True

    user_plane.armor_bar.draw_bar(screen)
    user_plane.health_bar.draw_bar(screen)

    pg.display.flip()

pg.quit()
