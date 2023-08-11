#!/usr/bin/python3
import pygame
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
from game.planes.control_enemies import EnemyController
from game.planes.enemy_tower import Tower
from bar import Bar

sys.path.append(r'..')

user_settings = get_game_settings()

fps = int(user_settings.get("fps"))

user_plane = UserPlane(pg.image.load('../images/user_plane_images/user_plane_1.png').convert_alpha())
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

health_bar = Bar(500, 760, 145, 25, 100, (110, 137, 181), (21, 43, 79))  # last two tuples are rgb colour codes
armour_bar = Bar(740, 760, 145, 25, 100, (110, 137, 181), (21, 43, 79))  # last two tuples are rgb colour codes

running = True
while running:
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        elif event.type == SPAWN_ENEMY_PLANE:
            random_image = helpers.get_random_image_of_enemy_planes(enemy_planes_surface_objects)
            enemies.add_enemy(EnemyPlane(random_image))

        elif event.type == SPAWN_TOWER:
            enemies.add_enemy(Tower(tower_img))

    background.loop_background(screen)

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_1] and health_bar.current_health:
        health_bar.reduce_bar()
    health_bar.draw_bar(screen)

    if keys_pressed[pygame.K_2] and armour_bar.current_health:
        armour_bar.reduce_bar()
    armour_bar.draw_bar(screen)

    enemies.update_planes(screen)
    enemies.update_towers(screen, user_plane)

    user_plane.functionality()
    user_plane.display_plane(screen)
    user_plane.update_shot_bullets(screen)

    pg.display.flip()

pg.quit()
