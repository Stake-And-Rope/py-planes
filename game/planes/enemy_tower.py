import math
import pygame as pg

from game.bullets.tower_bullet import TowerBullet
from game.helpers import (get_screen_dimensions,
                          calculate_center,
                          get_enemy_plane_speed
                          )
from game.planes.base_plane import BasePlane

SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_dimensions()


class Tower(BasePlane):
    plane_speed = get_enemy_plane_speed(BasePlane.GAME_FPS)

    def __init__(self, tower_img):
        super().__init__(tower_img)
        self.shoot_bullets_amount = 1
        self.weapon_width = 8
        self.weapon_length = 40

    @property
    def get_weapons_locations(self):
        center_x = calculate_center(self.width, self.weapon_width) + self.x_pos + self.weapon_width // 2
        center_y = calculate_center(self.height, self.weapon_width) + self.y_pos + self.weapon_width // 2
        return center_x, center_y


    @property
    def get_shoot_cd(self):
        return 1.3

    def set_spawn_point(self, x_pos: int, y_pos: int):
        error_message = ""
        if y_pos != -self.height:
            error_message = f"Tower must be spawned at {-self.height} pixels of Y coordinate."

        if x_pos < 0 or x_pos > SCREEN_WIDTH - self.width:
            error_message = f"Tower X coordinates must be between 0 and {SCREEN_WIDTH - self.width} pixels."

        if any(not isinstance(x, int) for x in (x_pos, y_pos)):
            error_message = "Coordinates must be integer values."

        if error_message:
            raise ValueError(error_message)

        self.x_pos = x_pos
        self.y_pos = y_pos

    def get_fire_bullet_exit_point(self, user_plane):
        tower_x, tower_y = self.get_weapons_locations

        direction = (user_plane.x_pos + (user_plane.rect.width // 2) - tower_x,
                     user_plane.y_pos + (user_plane.rect.height // 2) - tower_y)

        distance = math.sqrt(direction[0] ** 2 + direction[1] ** 2)

        normalized_direction = (direction[0] / distance, direction[1] / distance)

        scaled_direction = (normalized_direction[0] * self.weapon_length, normalized_direction[1] * self.weapon_length)

        line_endpoint = (tower_x + scaled_direction[0], tower_y + scaled_direction[1])

        return line_endpoint

    def functionality(self,screen, user_plane):
        self.y_pos += self.plane_speed

        if self.can_shoot_bullet:
            self.shoot_bullet(user_plane)

        if not self.can_shoot_bullet:
            self.lower_shoot_cooldown()

        pg.draw.line(screen,
                     (0, 0, 0), # color
                     self.get_weapons_locations, # start of line
                     self.get_fire_bullet_exit_point(user_plane), # end of line
                     self.weapon_width # line thickness
                     )

    def shoot_bullet(self, user_plane):
        bullet_x, bullet_y = self.get_fire_bullet_exit_point(user_plane)

        bullet = TowerBullet(bullet_x=bullet_x,
                             bullet_y=bullet_y,
                             target=user_plane,
                             )

        self.bullets.append(bullet)

        self.shooting_cooldown = self.get_shoot_cd

    def remove_out_of_boundary_bullets(self):
        on_screen_bullets = []

        for bullet in self.bullets:
            if bullet.bullet_x > SCREEN_WIDTH:
                continue

            if bullet.bullet_x + bullet.rect.width < 0:
                continue

            if bullet.bullet_y + bullet.rect.height < 0:
                continue

            if bullet.bullet_y > SCREEN_HEIGHT:
                continue

            on_screen_bullets.append(bullet)

        self.bullets = on_screen_bullets