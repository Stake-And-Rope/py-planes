#!/usr/bin/python3

import pygame as pg
import sys

from game.background_loop import BackgroundLoop
from game.planes.base_plane import Plane
from settings.settings_handler import get_game_settings
from game import helpers



sys.path.append(r'..')
pg.init()

window_size = helpers.get_screen_dimensions()
screen = pg.display.set_mode(window_size)

user_settings = get_game_settings()

fps = int(user_settings.get("fps"))
plane_speed = helpers.get_plane_speed(fps)


green_plane = Plane(
    '../images/user_plane_images/user_plane_1.png',
    plane_speed
    )

green_plane.set_spawn_point(
    helpers.calculate_center(window_size[0], green_plane.model.get_width()),
    650
    )


background = BackgroundLoop(fps)


clock = pg.time.Clock()

running = True
while running:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    background.loop_background(screen)

    green_plane.plane_movement()
    green_plane.display_plane(screen)

    pg.display.flip()

pg.quit()
