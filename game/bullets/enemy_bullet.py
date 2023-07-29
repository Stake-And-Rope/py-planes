from game.bullets.bullet import Bullet
from pygame import image


class EnemyBullet(Bullet):
    image = image.load("../images/enemy_plane_images/enemy_bullet.png").convert_alpha()

    def __init__(self, bullet_x: float, bullet_y: float):
        super().__init__(bullet_x, bullet_y)

    def move_bullet(self):
        self.bullet_y += self.bullet_speed