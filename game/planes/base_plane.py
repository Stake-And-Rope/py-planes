#!/usr/bin/python3
from abc import (ABC,
                 abstractmethod,
                 )

import pygame as pg

from game import helpers
from game.helpers import get_screen_dimensions
from settings.settings_handler import get_game_settings

SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_dimensions()


class BasePlane(ABC):
    GAME_FPS = int(get_game_settings().get("fps"))
    plane_speed = helpers.get_plane_speed(GAME_FPS)

    def __init__(self, model: str):
        self.model = pg.image.load(model).convert_alpha()
        self.rect = self.model.get_rect()
        self.height = self.rect.height
        self.width = self.rect.width
        self.fly_speed = self.plane_speed
        self.x_pos = None
        self.y_pos = None

        self.shoot_bullets_amount = 2
        self.shooting_cooldown = 0
        self.bullets = []

    @property
    @abstractmethod
    def get_weapons_locations(self):
        pass

    @property
    @abstractmethod
    def get_shoot_cd(self):
        pass

    @property
    def can_shoot_bullet(self):
        return self.shooting_cooldown <= 0

    @property
    def get_plane_pos(self):
        """
        returns tuple (x, y) to make it easier to image blit
        """
        return self.x_pos, self.y_pos

    @abstractmethod
    def set_spawn_point(self, x_pos: int, y_pos: int):
       pass

    @abstractmethod
    def check_plane_boundaries(self):
        pass

    @abstractmethod
    def plane_functionality(self):
        pass

    @abstractmethod
    def shoot_bullet(self):
        pass

    @abstractmethod
    def remove_out_of_boundary_bullets(self):
        pass

    def lower_shoot_cooldown(self):
        self.shooting_cooldown -= 1 / self.GAME_FPS

        if self.can_shoot_bullet:
            self.shooting_cooldown = 0

    def update_shot_bullets(self, screen):
        """
        1. looping through all the bullets on the screen
        2. updating the shot bullet
        3. displaying each bullet on screen
        4. removing the bullets which went out of the screen
        """

        for bullet in self.bullets:
            bullet.move_bullet()
            screen.blit(bullet.image, bullet.get_bullet_pos)

        self.remove_out_of_boundary_bullets()

    def display_plane(self, window):
        window.blit(self.model, self.get_plane_pos)
