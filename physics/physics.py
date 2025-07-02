from physics.collision_handler import *

def apply_gravity(player, gravity=0.8):
    if not player.on_ground:
        player.vel_y += gravity
        player.y += player.vel_y
    else:
        player.vel_y = 0

def apply_movement(player):
    player.x += player.vel_x
    player.vel_x = 0

def apply_collision(player, ground, platforms):
    if check_ground_collision(player, ground.get_top()):
        player.y = ground.get_top() - player.height
        player.on_ground = True
        return

    for platform in platforms:

        if check_platform_collision(player, platform):

            if platform.solid:
                solid_platform_collisions_handler(player, platform)
                return

            else:
                if player.y < platform.y - platform.height:
                    player.y = platform.y - player.height
                    player.on_ground = True
                else:
                    player.on_ground = False
                return
 
    player.on_ground = False
