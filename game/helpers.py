def get_plane_speed(fps: int) -> float:
    plane_speed = {
        45: 4.5,
        60: 3.5,
        75: 2.5,
    }

    return plane_speed.get(fps)