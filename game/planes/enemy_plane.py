from game.planes.base_plane import BasePlane


class EnemyPlane(BasePlane):

    def __init__(self, model):
        super().__init__(model)

    @property
    def get_weapons_locations(self):
        pass

    def set_spawn_point(self, x_pos: int, y_pos: int):
        pass

    def check_plane_boundaries(self):
        pass

    def plane_functionality(self):
        pass

    def shoot_bullet(self):
        pass

    def remove_bullet_if_out_of_boundary(self):
        pass