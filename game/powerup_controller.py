class PowerupController:

    def __init__(self):
        self.extra_bullets = None

    def render_extra_bullets(self, screen, user_plane):
        if self.extra_bullets is None:
            return

        self.extra_bullets.render(screen=screen)

        if self.extra_bullets.collide(plane=user_plane):
            self.extra_bullets.reset_position()
            user_plane.receive_extra_bullets()
            self.extra_bullets = None