from game.helpers import random_enemy_plane_coordinates
from game.planes.enemy_plane import EnemyPlane
from game.planes.enemy_tower import Tower


class EnemyController:

    def __init__(self):
        self.enemy_planes = []
        self.towers = []

    def add_enemy(self, enemy):
        random_x_spawn = random_enemy_plane_coordinates()
        enemy.set_spawn_point(*random_x_spawn)
        enemy.create_health_bar()
        enemy.create_armor_bar()

        if isinstance(enemy, EnemyPlane):
            self.enemy_planes.append(enemy)

        elif isinstance(enemy, Tower):
            self.towers.append(enemy)

    def update_planes(self, screen):
        for plane in self.enemy_planes:
            plane.functionality()
            plane.health_bar.draw_bar(window=screen, hide_bar_when_empty=True)
            plane.display_plane(screen)
            plane.update_shot_bullets(screen)

    def update_towers(self, screen, user_plane):
        for tower in self.towers:
            tower.health_bar.draw_bar(window=screen, hide_bar_when_empty=True)
            tower.display_plane(screen)
            tower.functionality(screen, user_plane)
            tower.update_shot_bullets(screen)