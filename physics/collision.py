import pygame

def check_platform_collision(player, platform):
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
    return player_rect.colliderect(platform.get_rect())

def check_ground_collision(player, ground):
    return player.y + player.height >= ground