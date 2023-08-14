#!/usr/bin/python3
from abc import (ABC,
                 abstractmethod,
                 )

import pygame as pg
from pygame import Surface

from game import helpers
from game.helpers import get_screen_dimensions
from settings.settings_handler import get_game_settings

SCREEN_WIDTH, SCREEN_HEIGHT = get_screen_dimensions()
from game.float_rect import FloatRect
from game.bar import Bar


class BasePlane(ABC):
    GAME_FPS = int(get_game_settings().get("fps"))
    plane_speed = helpers.get_plane_speed(GAME_FPS)

    def __init__(self, model: Surface, health: int, armor: int, damage: int):
        self.model = model
        self.plane_mask = pg.mask.from_surface(model)
        self.regular_rect = self.model.get_rect()
        self.height = self.regular_rect.height
        self.width = self.regular_rect.width
        self.float_rect = FloatRect(None, None, self.width, self.height)
        self.x_pos = None
        self.y_pos = None

        self.health = health
        self.armor = armor
        self.damage = damage

        self.enemy_bar_width = self.width // 1.2
        self.enemy_bar_height = 10

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
    def remove_out_of_boundary_bullets(self):
        pass

    def auto_create_enemy_health_bar(self):
        bar = Bar(x=helpers.calculate_center(self.width, self.enemy_bar_width) + self.x_pos,
                  y=self.y_pos - self.enemy_bar_height,
                  width=self.enemy_bar_width,
                  height=self.enemy_bar_height,
                  max_value=self.health,
                  top_colour=(0, 153, 0),
                  bottom_colour=(128, 128, 128),
                  )
        setattr(self, "enemy_health_bar", bar)
        setattr(self, "enemy_gap_on_both_ends_of_bar", bar.x - self.x_pos)

    def auto_create_enemy_armor_bar(self):
        bar = Bar(x=helpers.calculate_center(self.width, self.enemy_bar_width) + self.x_pos,
                  y=self.y_pos - self.enemy_bar_height,
                  width=self.enemy_bar_width,
                  height=self.enemy_bar_height,
                  max_value=self.armor,
                  top_colour=(21, 43, 79),
                  bottom_colour=(128, 128, 128),
                  )
        setattr(self, "enemy_armor_bar", bar)

    def create_user_bar(self,
                        bar_type: str,
                        x: float,
                        y: float,
                        width: int,
                        height: int,
                        max_value: int,
                        top_color: tuple,
                        bottom_color: tuple):
        bar = Bar(x=x,
                  y=y,
                  width=width,
                  height=height,
                  max_value=max_value,
                  top_colour=top_color,
                  bottom_colour=bottom_color,
                  )
        setattr(self, bar_type, bar)

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
