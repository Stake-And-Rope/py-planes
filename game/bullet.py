from pygame import image


class Bullet:

    def __init__(self, plane_x: float, plane_y: float):
        self.image = image.load("../images/user_plane_images/user_bullet.png").convert_alpha()
        self.plane_x = plane_x
        self.plane_y = plane_y

        self.bullet_x, self.bullet_x_two = self.set_bullets_location()
        self.bullet_y = self.plane_y

    @property
    def get_first_bullet_pos(self):
        return self.bullet_x, self.bullet_y

    @property
    def get_second_bullet_pos(self):
        return self.bullet_x_two, self.bullet_y

    def set_bullets_location(self) -> tuple:
        left_bullet = self.plane_x + 10
        right_bullet = self.plane_x + 50
        return left_bullet, right_bullet

    def move_bullet(self):
        self.bullet_y -= 3




