# player.py
from entities.base_entity import BaseEntity

BLUE = (50, 50, 255)

class Player(BaseEntity):
    def __init__(self, x, y, width=50, height=60, color=BLUE):
        super().__init__(x, y, width, height, color)

        self.vel_x = 0
        self.vel_y = 0

        self.jump_power = -15
        self.run_power = 10

        self.on_ground = True
        self.hit_left_wall = False
        self.hit_right_wall = False

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def move_left(self):
        if not self.hit_left_wall:
            self.vel_x = -self.run_power

    def move_right(self):
        if not self.hit_right_wall:
            self.vel_x = +self.run_power
