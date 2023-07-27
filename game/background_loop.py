from pygame import image

from game.helpers import get_background_roll_speed


class BackgroundLoop:
    def __init__(self, fps: int):
        self.background = image.load('../images/environment/ocean.png').convert_alpha()
        self.background_rect = self.background.get_rect()

        self.background_y_1 = 0
        self.x = 0

        self.background_y_2 = self.background_rect.height

        self.roll_speed = get_background_roll_speed(fps)

    def update(self):
        self.background_y_1 += self.roll_speed
        self.background_y_2 += self.roll_speed

        rect_height = self.background_rect.height

        if self.background_y_1 >= rect_height:
            self.background_y_1 = -rect_height

        if self.background_y_2 >= rect_height:
            self.background_y_2 = -rect_height

    def render(self, window):
        window.blit(self.background, (self.x, self.background_y_1))
        window.blit(self.background, (self.x, self.background_y_2))

    def loop_background(self, window):
        self.update()
        self.render(window)