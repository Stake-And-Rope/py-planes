import random

from game.bullets.enemy_bullet import EnemyBullet
from game.helpers import (get_screen_dimensions,
                          get_enemy_plane_speed,
                          )
from game.planes.base_plane import BasePlane

SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_dimensions()


class EnemyPlane(BasePlane):
    plane_speed = get_enemy_plane_speed(BasePlane.GAME_FPS)

    def __init__(self, model, health, armor, damage):
        super().__init__(model, health, armor, damage)
        self.x_direction = 0
        self.distance_until_next_direction = 0
        self.change_direction_every_traveled_pixels = 300

    @property
    def get_shoot_cd(self):
        return 1.5

    @property
    def get_weapons_locations(self):
        """
        :return: (
                  (left_outer_weapon, plane_y),
                  (right_outer_weapon, plane_y),
                  (left_inner_weapon, plane_y),
                  (right_inner_weapon, plane_y)
                 )
        """

        y_pos = self.y_pos + self.height - 6

        inner_weapons_pos = ((self.x_pos + 11, y_pos), (self.x_pos + 50, y_pos))
        outer_weapons_pos = ((self.x_pos + 6, y_pos), (self.x_pos + 56, y_pos))

        return outer_weapons_pos + inner_weapons_pos

    @property
    def is_below_screen(self):
        return self.y_pos > SCREEN_HEIGHT

    @property
    def can_change_direction(self):
        return self.distance_until_next_direction <= 0

    def random_enemy_plane_direction(self):
        direction = random.choice(
            (self.plane_speed, -self.plane_speed)
        )

        self.x_direction = direction

    def handle_x_direction(self):
        self.distance_until_next_direction -= abs(self.x_direction) + self.plane_speed

        if self.can_change_direction:
            self.random_enemy_plane_direction()
            self.distance_until_next_direction = self.change_direction_every_traveled_pixels

    def set_spawn_point(self, x_pos: int, y_pos: int):
        error_message = ""
        if y_pos != -self.height:
            error_message = f"Plane must be spawned at {-self.height} pixels of Y coordinate."

        if x_pos < 0 or x_pos > SCREEN_WIDTH - self.width:
            error_message = f"Plane X coordinates must be between 0 and {SCREEN_WIDTH - self.width} pixels."

        if any(not isinstance(x, int) for x in (x_pos, y_pos)):
            error_message = "Coordinates must be integer values."

        if error_message:
            raise ValueError(error_message)

        self.x_pos = x_pos
        self.y_pos = y_pos

        self.float_rect.x = x_pos
        self.float_rect.y = y_pos

    def check_plane_boundaries(self):
        right_border = SCREEN_WIDTH - self.float_rect.width

        if self.x_pos < 0:
            self.x_pos = 0
            self.float_rect.x = 0
            self.enemy_health_bar.x = self.enemy_gap_on_both_ends_of_bar
            self.enemy_armor_bar.x = self.enemy_gap_on_both_ends_of_bar

        elif self.x_pos >= right_border:
            self.x_pos = right_border
            self.float_rect.x = right_border
            self.enemy_health_bar.x = right_border + self.enemy_gap_on_both_ends_of_bar
            self.enemy_armor_bar.x = right_border + self.enemy_gap_on_both_ends_of_bar

    def functionality(self):
        self.y_pos += self.plane_speed
        self.x_pos += self.x_direction

        self.float_rect.y += self.plane_speed
        self.float_rect.x += self.x_direction

        self.enemy_health_bar.x += self.x_direction
        self.enemy_health_bar.y += self.plane_speed

        self.enemy_armor_bar.x += self.x_direction
        self.enemy_armor_bar.y += self.plane_speed

        if self.can_shoot_bullet:
            self.shoot_bullet()

        if not self.can_shoot_bullet:
            self.lower_shoot_cooldown()

        self.check_plane_boundaries()
        self.handle_x_direction()

    def shoot_bullet(self):
        for wep_x, wep_y in self.get_weapons_locations[:self.shoot_bullets_amount]:
            create_bullet = EnemyBullet(wep_x, wep_y)

            self.bullets.append(create_bullet)

        self.shooting_cooldown = self.get_shoot_cd

    def remove_out_of_boundary_bullets(self):
        self.bullets = [bullet for bullet in self.bullets if bullet.float_rect.height + bullet.bullet_y < SCREEN_HEIGHT]

