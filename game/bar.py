import pygame


class Bar:
    def __init__(self, x, y, width, height, max_value, top_colour, bottom_colour):
        self.x = x
        self.y = y
        self.width = width
        self.current_width = width
        self.height = height
        self.max_value = max_value
        self.current_value = max_value
        self.top_colour = top_colour
        self.bottom_colour = bottom_colour

    def draw_bar(self, window, hide_bar_when_empty=False):
        if self.current_value <= 0 and hide_bar_when_empty:
            return

        pygame.draw.rect(window, self.bottom_colour, (self.x, self.y, self.width, self.height), border_radius=3)
        pygame.draw.rect(window, self.top_colour, (self.x, self.y, self.current_width, self.height), border_radius=3)

    def reduce_bar(self, damage_value):
        self.current_value -= damage_value
        self.lower_upper_bar_width()

    def increase_bar(self, increase_value):
        self.current_value += increase_value

    def lower_upper_bar_width(self):
        result_width = (self.current_value / self.max_value) * self.width

        if result_width <= 0:
            self.current_width = 0
        else:
            self.current_width = result_width
