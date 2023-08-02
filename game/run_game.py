#!/usr/bin/python3

import pygame as pg

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

sys.path.append(r'..')

user_settings = get_game_settings()

fps = int(user_settings.get("fps"))

green_plane = UserPlane('../images/user_plane_images/user_plane_1.png')
green_plane.set_spawn_point(
    helpers.calculate_center(window_size[0], green_plane.model.get_width()),
    650
    )

background = BackgroundLoop(fps)
clock = pg.time.Clock()

SPAWN_ENEMY = pg.USEREVENT + 1
pg.time.set_timer(SPAWN_ENEMY, 5000)

enemy = EnemyPlane("../images/enemy_plane_images/enemy_plane_1.png")
enemy.set_spawn_point(400, -64)

running = True
while running:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == SPAWN_ENEMY:
            print("Spawn enemy plane")

    background.loop_background(screen)

    enemy.plane_functionality()
    enemy.display_plane(screen)
    enemy.update_shot_bullets(screen)

    green_plane.plane_functionality()
    green_plane.display_plane(screen)

    green_plane.update_shot_bullets(screen)

    pg.display.flip()

pg.quit()
