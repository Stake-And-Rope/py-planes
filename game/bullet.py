from pygame import image

from game.helpers import get_bullet_speed
from settings.settings_handler import get_game_settings


fps = int(get_game_settings().get("fps"))
bullet_speed = get_bullet_speed(fps)


class Bullet:
    image = image.load("../images/user_plane_images/user_bullet.png").convert_alpha()

    def __init__(self, bullet_x: float, bullet_y: float):
        self.bullet_x = bullet_x
        self.bullet_y = bullet_y

    @property
    def get_bullet_pos(self):
        return self.bullet_x, self.bullet_y

    def move_bullet(self):
        self.bullet_y -= bullet_speed




