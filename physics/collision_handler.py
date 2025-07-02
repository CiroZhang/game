from physics.collision import *
from physics.locations import *

def solid_platform_collisions_handler(player, platform):
    x_status, y_status = compare_player_and_platform_location(player, platform)
    plat_top, plat_bottom, plat_left, plat_right = get_platform_edge_locations(platform)

    if y_status == "below":
        player.vel_y = 0
        player.y = plat_bottom

    if y_status == "above":
        player.vel_y = 0
        player.y = plat_top - player.height
        player.on_ground = True

    if x_status == "left":
        player.x = plat_left
        player.hit_left_wall = True

    if x_status == "right":
        player.x = plat_right - player.width