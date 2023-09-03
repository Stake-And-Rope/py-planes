from game.float_rect import float_rects_collide


def collision(curr_enemy, curr_plane):
    not_collided_bullets = []

    for bullet in curr_enemy.bullets:
        if float_rects_collide(bullet.float_rect, curr_plane.float_rect):
            bullet_mask = bullet.bullet_mask
            user_plane_mask = curr_plane.plane_mask

            if not user_plane_mask.overlap(bullet_mask,
                                       (int(bullet.float_rect.x) - int(curr_plane.float_rect.x), int(bullet.float_rect.y) - int(curr_plane.float_rect.y))):
                not_collided_bullets.append(bullet)
        else:
            not_collided_bullets.append(bullet)

    if len(not_collided_bullets) < len(curr_enemy.bullets):
        len_all_enemy_bullets, len_all_not_collided_bullets = len(curr_enemy.bullets), len(not_collided_bullets)
        curr_enemy.bullets = not_collided_bullets
        return len_all_enemy_bullets - len_all_not_collided_bullets

    return False


def check_user_plane_collision(all_enemies, c_user_plane):
    REDUCE_TIMES_USER_PLANE = 1

    for enemy_plane in all_enemies.enemy_planes:
        enemy_planes_damage = collision(enemy_plane, c_user_plane)

        if c_user_plane.armor_bar.current_width == 0:
            c_user_plane.health_bar.reduce_bar(1 * enemy_planes_damage)
        else:
            c_user_plane.armor_bar.reduce_bar(1 * enemy_planes_damage)

    for enemy_tower in all_enemies.towers:
        towers_damage = collision(enemy_tower, c_user_plane)

        if c_user_plane.armor_bar.current_width == 0:
            c_user_plane.health_bar.reduce_bar(REDUCE_TIMES_USER_PLANE * towers_damage)
        else:
            c_user_plane.armor_bar.reduce_bar(REDUCE_TIMES_USER_PLANE * towers_damage)


def check_enemy_collision(all_enemies, c_user_plane):
    REDUCE_TIMES_ENEMY_OR_TOWER = 5

    for enemy_plane in all_enemies.enemy_planes:
        damage = collision(c_user_plane, enemy_plane)

        enemy_plane.enemy_health_bar.reduce_bar(REDUCE_TIMES_ENEMY_OR_TOWER * damage)

    for enemy_tower in all_enemies.towers:
        damage = collision(c_user_plane, enemy_tower)

        enemy_tower.enemy_health_bar.reduce_bar(REDUCE_TIMES_ENEMY_OR_TOWER * damage)


def check_user_plane_and_enemies_collision(all_enemies, c_user_plane):
    curr_enemies = all_enemies.enemy_planes + all_enemies.towers

    for enemy_plane in curr_enemies:
        if float_rects_collide(enemy_plane.float_rect, c_user_plane.float_rect):
            enemy_plane_mask = enemy_plane.plane_mask
            user_plane_mask = c_user_plane.plane_mask

            if user_plane_mask.overlap(enemy_plane_mask,
                                           (int(enemy_plane.float_rect.x) - int(c_user_plane.float_rect.x),
                                            int(enemy_plane.float_rect.y) - int(c_user_plane.float_rect.y))):
                return True