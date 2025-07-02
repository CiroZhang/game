# player.py
import pygame
from entities.base_entity import BaseEntity

BLUE = (50, 50, 255)

class Player(BaseEntity):
    def __init__(self, x, y, width=100, height=60, color=BLUE):
        super().__init__(x, y, width, height, color)

        self.vel_x = 0
        self.vel_y = 0

        self.jump_power = -15
        self.run_power = 10

        self.on_ground = True
        self.hit_left_wall = False
        self.hit_right_wall = False

        self.direction = "right"

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_power
            self.on_ground = False

    def move_left(self):
        self.direction = "left"
        if not self.hit_left_wall:
            self.vel_x = -self.run_power

    def move_right(self):
        self.direction = "right"
        if not self.hit_right_wall:
            self.vel_x = +self.run_power

    def draw(self, screen):
        if self.direction == "left":
            if self.on_ground:
                self.image = pygame.image.load("assets/player(left).png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.width, self.height))

            else: 
                self.image = pygame.image.load("assets/player(jump_left).png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.width, self.height*1.8))

        if self.direction == "right":
            if self.on_ground:
                self.image = pygame.image.load("assets/player(right).png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.width, self.height))

            else: 
                self.image = pygame.image.load("assets/player(jump_right).png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.width, self.height*1.8))

        screen.blit(self.image, (self.x, self.y))
