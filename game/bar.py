import pygame


class Bar:
    def __init__(self, x, y, width, height, max_value, top_colour, bottom_colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_value = max_value
        self.current_value = max_value
        self.top_colour = top_colour
        self.bottom_colour = bottom_colour

    def draw_bar(self, window):
        current_health_to_max_health = self.current_value / self.max_value

        pygame.draw.rect(window, self.top_colour, (self.x, self.y, self.width, self.height), border_radius=3)
        pygame.draw.rect(window, self.bottom_colour, (self.x, self.y, current_health_to_max_health * self.width, self.height), border_radius=3)

    def reduce_bar(self):
        self.current_value -= 1
