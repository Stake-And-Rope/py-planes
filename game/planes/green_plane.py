from game.planes.base_plane import BasePlane


class GreenPlane(BasePlane):

    def __init__(self,
                 model: str,
                 fly_speed: float):
        super().__init__(model, fly_speed)