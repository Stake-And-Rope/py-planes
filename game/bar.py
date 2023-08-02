import pygame


class Bar:
    def __init__(self, x, y, width, height, max_health, first_colour, second_colour):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = max_health
        self.current_health = max_health
        self.first_colour = first_colour
        self.second_colour = second_colour

    def draw_bar(self, window):
        current_health_to_max_health = self.current_health / self.max_health

        pygame.draw.rect(window, self.first_colour, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(window, self.second_colour, (self.x, self.y, current_health_to_max_health * self.width, self.height))

    def reduce_health_bar(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_1]:
            self.current_health -= 1

    def reduce_armour_bar(self):
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_2]:
            self.current_health -= 1