#!/usr/bin/python3

import pygame as pg

from game.helpers import get_screen_dimensions


class Plane:
    LEFT_RIGHT_KEYS = ("a", "d")
    UP_DOWN_KEYS = ("w", "s")

    def __init__(self,
                 model: str,
                 fly_speed: float):

        self.model = pg.image.load(model).convert_alpha()
        self.rect = self.model.get_rect()
        self.height = self.rect.height
        self.width = self.rect.width
        self.fly_speed = fly_speed
        self.x_pos = None
        self.y_pos = None

    @property
    def middle_screen_border(self):
        height = get_screen_dimensions()[1]
        return height // 2.5

    @property
    def get_plane_pos(self):
        """
        returns tuple (x, y) to make it easier to image blit
        """
        return self.x_pos, self.y_pos

    @property
    def move_directions(self):
        """
        map to get the buttons and the direction
        """
        return {
            pg.key.key_code(self.LEFT_RIGHT_KEYS[0]): -self.fly_speed,
            pg.key.key_code(self.LEFT_RIGHT_KEYS[1]): self.fly_speed,
            pg.key.key_code(self.UP_DOWN_KEYS[0]): -self.fly_speed,
            pg.key.key_code(self.UP_DOWN_KEYS[1]): self.fly_speed,
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

    def display_plane(self, window):
        window.blit(self.model, self.get_plane_pos)

    def check_plane_boundaries(self):
        """
        this method checks the following borders:

            1. left border (trying to get out of the screen from the left side)
            2. right border (trying to get out of the screen from the right side)
            3. bottom border (trying to get out of the screen from the bottom side)
            4. middle border (trying to get above the invisible border in the middle)

        if out of border, the plane will get returned in the border.
        """
        screen_width, screen_height = get_screen_dimensions()

        right_border = screen_width - self.width
        bottom_border = screen_height - self.height

        if self.x_pos < 0:
            self.x_pos = 0

        elif self.x_pos > right_border:
            self.x_pos = right_border

        if self.y_pos < self.middle_screen_border:
            self.y_pos = self.middle_screen_border

        elif self.y_pos > bottom_border:
            self.y_pos = bottom_border

    def plane_movement(self):
        """
        updates the coordinates of the plane if the correct keys are pressed
        """
        button_press = pg.key.get_pressed()

        for button in self.move_directions:
            if button_press[button] and pg.key.name(button) in self.LEFT_RIGHT_KEYS:
                self.x_pos += self.move_directions[button]

            if button_press[button] and pg.key.name(button) in self.UP_DOWN_KEYS:
                self.y_pos += self.move_directions[button]

            self.check_plane_boundaries()
