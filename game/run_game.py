#!/usr/bin/python3

import pygame as pg
import sys
from settings.settings_handler import get_game_settings
from game import helpers
from planes.green_plane import GreenPlane


sys.path.append(r'..')
pg.init()

window_size = (900, 800)
screen = pg.display.set_mode(window_size)

user_settings = get_game_settings()

fps = int(user_settings.get("fps"))
plane_speed = helpers.get_plane_speed(fps)

green_plane = GreenPlane(
    '../images/user_plane_images/base_plane.png',
    plane_speed
)
green_plane.set_spawn_point(250, 250)

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

    screen.fill((255, 255, 255))

    green_plane.plane_movement()

    screen.blit(green_plane.model, green_plane.get_plane_pos)

    pg.display.flip()

pg.quit()
