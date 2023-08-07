from game.bullets.bullet import Bullet


class UserBullet(Bullet):

    def __init__(self, bullet_x: float, bullet_y: float):
        super().__init__(bullet_x, bullet_y)

    def move_bullet(self):
        self.bullet_y -= self.bullet_speed
        self.rect.y -= self.bullet_speed