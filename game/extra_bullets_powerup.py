from random import randint

from pygame import Surface

from game import float_rect as rect
from helpers import get_screen_dimensions

SCREEN_WIDTH, _ = get_screen_dimensions()


class ExtraBulletsPowerUp:

    def __init__(self, image: Surface):
        self.image = image
        self.rect = self.image.get_rect()

        self.start_x = self.random_x_spawn()
        self.start_y = -self.rect.height

        self.float_rect = rect.FloatRect(x=self.start_x,
                                         y=self.start_y,
                                         width=self.rect.width,
                                         height=self.rect.height
                                         )

        self.drop_speed = 3

    def random_x_spawn(self):
        return randint(0, SCREEN_WIDTH - self.rect.width)

    def reset_position(self):
        self.float_rect.x = self.start_x
        self.float_rect.y = self.start_y

    def render(self, screen):
        self.float_rect.y += self.drop_speed

        screen.blit(self.image, (self.float_rect.x, self.float_rect.y))

    def collide(self, plane):
        return rect.float_rects_collide(self.float_rect, plane.float_rect)