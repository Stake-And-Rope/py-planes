#!/usr/bin/python3

import pygame as pg
from abc import (ABC,
                 abstractmethod,
                 )


class BasePlane(ABC):
    LEFT_RIGHT_KEYS = ("a", "d")
    UP_DOWN_KEYS = ("w", "s")

    def __init__(self,
                 model: str,
                 fly_speed: float):

        self.model = pg.image.load(model).convert_alpha()
        self.fly_speed = fly_speed
        self.x_pos = None
        self.y_pos = None

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
        raises value error if one of the args is not integer
        """

        if any(not isinstance(value, int) for value in (x_pos, y_pos)):
            raise ValueError("Values must be integers")

        self.x_pos = x_pos
        self.y_pos = y_pos

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
