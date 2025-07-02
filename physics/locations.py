def get_player_edge_locations(player):
    top = player.y
    bottom = player.y + player.height
    left = player.x
    right = player.x + player.width
    return top, bottom, left, right

def get_platform_edge_locations(platform):
    top = platform.y
    bottom = platform.y + platform.height
    left = platform.x
    right = platform.x + platform.width
    return top, bottom, left, right


def compare_player_and_platform_location(player, platform):
    x_status = None
    y_status = None

    p_top, p_bottom, p_left, p_right = get_player_edge_locations(player)
    plat_top, plat_bottom, plat_left, plat_right = get_platform_edge_locations(platform)
    
    if p_right < plat_left + 5:
        x_status = "left"
    elif p_left > plat_right - 5:
        x_status = "right"
    else:
        x_status = "overlap"

    if p_bottom <= plat_top + player.vel_y + 5:
        y_status = "above"
    elif p_top >= plat_bottom + player.vel_y - 5:
        y_status = "below"
    else:
        y_status = "overlap"

    return x_status, y_status