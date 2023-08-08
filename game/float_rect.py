class FloatRect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


def float_rects_collide(rect1, rect2):
    return (rect1.x < rect2.x + rect2.width and
            rect2.x < rect1.x + rect1.width and
            rect1.y < rect2.y + rect2.height and
            rect2.y < rect1.y + rect1.height)
