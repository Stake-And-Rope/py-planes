import pygame


class Bar:
    def __init__(self, x, y, width, height, max_health, top_colour, bottom_colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = max_health
        self.current_health = max_health
        self.top_colour = top_colour
        self.bottom_colour = bottom_colour

    def draw_bar(self, window):
        current_health_to_max_health = self.current_health / self.max_health

        pygame.draw.rect(window, self.top_colour, (self.x, self.y, self.width, self.height), border_radius=3)
        pygame.draw.rect(window, self.bottom_colour, (self.x, self.y, current_health_to_max_health * self.width, self.height), border_radius=3)

    def reduce_health_bar(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_1] and self.current_health:
            self.current_health -= 1

    def reduce_armour_bar(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_2] and self.current_health:
            self.current_health -= 1