from abc import (ABC,
                 abstractmethod
                 )

import pygame
from pygame import image

from game.helpers import get_bullet_speed
from settings.settings_handler import get_game_settings

from game.float_rect import FloatRect


fps = int(get_game_settings().get("fps"))
bullet_speed = get_bullet_speed(fps)


class Bullet(ABC):
    image = image.load("../images/user_plane_images/user_bullet.png").convert_alpha()
    bullet_speed = get_bullet_speed(fps)

    def __init__(self, bullet_x: float, bullet_y: float):
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y
        self.regular_rect = self.image.get_rect()
        self.image_width = self.regular_rect[2]
        self.image_height = self.regular_rect[3]
        self.float_rect = FloatRect(bullet_x, bullet_y, self.image_width, self.image_height)
        self.bullet_mask = pygame.mask.from_surface(self.image)

    @property
    def get_bullet_pos(self):
        return self.bullet_x, self.bullet_y

    @abstractmethod
    def move_bullet(self):
        pass
