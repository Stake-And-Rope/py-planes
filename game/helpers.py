def get_plane_speed(fps: int) -> float:
    plane_speed = {
        45: 4.5,
        60: 3.5,
        75: 2.5,
    }

    return plane_speed.get(fps)


def get_bullet_speed(fps: int) -> float:
    bullet_speed = {
        45: 4.5,
        60: 3.5,
        75: 2.5,
    }

    return bullet_speed.get(fps)


def get_background_roll_speed(fps: int) -> float:
    looping_speed = {
        45: 2,
        60: 1.6,
        75: 1.2,
    }

    return looping_speed.get(fps)


def calculate_center(main_obj_width, child_obj_width):
    """
    run this code to visually see how it is being calculated
    -- pygame.draw.rect(screen, (255, 0, 0), (window_size[0] // 2, 0, 1, window_size[1]), 1) --
    -- pg    .draw.rect(screen, (255, 0, 0), (window_size[0] // 2, 0, 1, window_size[1]), 1) --

    :return: int(pixels) of the X position where the child object must be placed
    """
    middle_of_main_obj = main_obj_width // 2
    middle_of_child_obj = child_obj_width // 2


    return middle_of_main_obj - middle_of_child_obj


def get_screen_dimensions() -> tuple:
    return 900, 800