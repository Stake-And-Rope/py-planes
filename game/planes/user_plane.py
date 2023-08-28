#!/usr/bin/python3

import pygame as pg

from game.bullets.user_bullet import UserBullet
from game.helpers import get_screen_dimensions
from game.planes.base_plane import BasePlane

SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_dimensions()

class UserPlane(BasePlane):
    LEFT_RIGHT_KEYS = ("a", "d")
    UP_DOWN_KEYS = ("w", "s")
    SHOOT_BUTTON = " "

    def __init__(self, model, health, armor, damage):
        super().__init__(model, health, armor, damage)

        self.extra_bullets_duration = 20
        self.duration_left = 0

    @property
    def get_shoot_cd(self):
        return 0.5

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

        inner_weapons_pos = ((self.x_pos + 11, self.y_pos), (self.x_pos + 50, self.y_pos))
        outer_weapons_pos = ((self.x_pos + 6, self.y_pos), (self.x_pos + 56, self.y_pos))

        return outer_weapons_pos + inner_weapons_pos

    @property
    def middle_screen_border(self):
        return SCREEN_HEIGHT // 2.5

    @property
    def move_directions(self):
        """
        map to get the buttons and the direction
        """
        return {
            pg.key.key_code(self.LEFT_RIGHT_KEYS[0]): -self.plane_speed,
            pg.key.key_code(self.LEFT_RIGHT_KEYS[1]): self.plane_speed,
            pg.key.key_code(self.UP_DOWN_KEYS[0]): -self.plane_speed,
            pg.key.key_code(self.UP_DOWN_KEYS[1]): self.plane_speed,
        }

    def set_spawn_point(self,
                        x_pos: int,
                        y_pos: int):
        """
        sets the x and y coordinates if the given args are integers
        raises value error if one of the args is not integer or if the args are with invalid destination
        """

        if any(not isinstance(value, int) for value in (x_pos, y_pos)):
            raise ValueError("Values must be integers.")

        if y_pos < self.middle_screen_border:
            raise ValueError(f"y_pos cannot be between 0 and {self.middle_screen_border} pixels.")

        screen_width, screen_height = get_screen_dimensions()

        if y_pos > screen_height - self.height:
            raise ValueError(f"y_pos must be between {self.middle_screen_border} and {screen_height - self.height} pixels.")


        if x_pos > screen_width - self.width or x_pos < 0:
            raise ValueError(f"x_pos must be between 0 and {screen_width - self.width} pixels.")


        self.x_pos = x_pos
        self.y_pos = y_pos

        self.float_rect.x = x_pos
        self.float_rect.y = y_pos

    def check_plane_boundaries(self):
        """
        this method checks the following borders:

            1. left border (trying to get out of the screen from the left side)
            2. right border (trying to get out of the screen from the right side)
            3. bottom border (trying to get out of the screen from the bottom side)
            4. middle border (trying to get above the invisible border in the middle)

        if out of border, the plane will get returned in the border.
        """

        right_border = SCREEN_WIDTH - self.width
        bottom_border = SCREEN_HEIGHT - self.height

        if self.x_pos < 0:
            self.x_pos = 0
            self.float_rect.x = 0

        elif self.x_pos > right_border:
            self.x_pos = right_border
            self.float_rect.x = right_border

        if self.y_pos < self.middle_screen_border:
            self.y_pos = self.middle_screen_border
            self.float_rect.y = self.middle_screen_border

        elif self.y_pos > bottom_border:
            self.y_pos = bottom_border
            self.float_rect.y = bottom_border

    def functionality(self):
        """
        updates the coordinates of the plane if the correct keys are pressed
        shoots bullets if the correct button is pressed and if there is no cooldown
        """

        button_press = pg.key.get_pressed()

        for button in self.move_directions:
            if button_press[button] and pg.key.name(button) in self.LEFT_RIGHT_KEYS:
                self.x_pos += self.move_directions[button]
                self.float_rect.x += self.move_directions[button]

            if button_press[button] and pg.key.name(button) in self.UP_DOWN_KEYS:
                self.y_pos += self.move_directions[button]
                self.float_rect.y += self.move_directions[button]

            self.check_plane_boundaries()

        if button_press[pg.key.key_code(self.SHOOT_BUTTON)] and self.can_shoot_bullet:
            self.shoot_bullet()

        if not self.can_shoot_bullet:
            self.lower_shoot_cooldown()

        self.lower_extra_bullets_duration()

    def shoot_bullet(self):
        """
        1. loops through the sliced tuple with the coordinates of the plane weapons
        2. creates a bullet for each weapon
        3. adds shoot cooldown after the bullets are fired
        """

        for wep_x, wep_y in self.get_weapons_locations[:self.shoot_bullets_amount]:
            create_bullet = UserBullet(wep_x, wep_y)

            self.bullets.append(create_bullet)

        self.shooting_cooldown = self.get_shoot_cd

    def remove_out_of_boundary_bullets(self):
        self.bullets = [bullet for bullet in self.bullets if bullet.bullet_y > 0]

    def receive_extra_bullets(self):
        self.shoot_bullets_amount = 4
        self.duration_left = self.extra_bullets_duration

    def extra_bullets_fade_away(self):
        self.shoot_bullets_amount = 2

    def lower_extra_bullets_duration(self):
        if self.duration_left > 0:
            self.duration_left -= 1 / self.GAME_FPS

            if self.duration_left <= 0:
                self.duration_left = 0
                self.extra_bullets_fade_away()
