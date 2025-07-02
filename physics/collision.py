import pygame

def check_platform_collision(player, platform):
    horizontal_overlap = (
        player.x + player.width > platform.x and
        player.x < platform.x + platform.width
    )

    vertical_overlap = (
        player.y + player.height >= platform.y and
        player.y < platform.y + platform.height
    )

    return horizontal_overlap and vertical_overlap

def check_ground_collision(player, ground):
    return player.y + player.height >= ground