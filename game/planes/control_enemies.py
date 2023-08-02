from game.helpers import random_enemy_plane_coordinates
from game.planes.enemy_plane import EnemyPlane


class EnemyController:

    def __init__(self):
        self.enemies = []

    def add_enemy(self, enemy):
        if isinstance(enemy, EnemyPlane):
            enemy.set_spawn_point(*random_enemy_plane_coordinates())

        self.enemies.append(enemy)

    def update_enemies(self, screen):
        for enemy in self.enemies:
            enemy.plane_functionality()
            enemy.display_plane(screen)
            enemy.update_shot_bullets(screen)