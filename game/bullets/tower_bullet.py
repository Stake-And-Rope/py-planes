import math

from game.bullets.bullet import Bullet
from pygame import image


class TowerBullet(Bullet):
    image = image.load("../images/enemy_plane_images/enemy_bullet.png").convert_alpha()

    def __init__(self,
                 bullet_x: float,
                 bullet_y: float,
                 target
                 ):
        super().__init__(bullet_x, bullet_y)
        self.target_x = target.x_pos
        self.target_y = target.y_pos
        self.target_rect = target.float_rect
        self.direction_radians = self.calculate_direction()

    def calculate_direction(self):
        return math.atan2(self.target_y + (self.target_rect.height // 2) - self.bullet_y,
                          self.target_x + (self.target_rect.width // 2) - self.bullet_x
                          )

    def move_bullet(self):
        self.bullet_x += self.bullet_speed * math.cos(self.direction_radians)
        self.bullet_y += self.bullet_speed * math.sin(self.direction_radians)

        self.float_rect.x += self.bullet_speed * math.cos(self.direction_radians)
        self.float_rect.y += self.bullet_speed * math.sin(self.direction_radians)
