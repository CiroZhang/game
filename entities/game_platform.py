from entities.base_entity import BaseEntity
import pygame

GREEN = (0, 200, 0)

class Platform(BaseEntity):
    def __init__(self, x, y, width, height=20, color=GREEN, solid=True):
        super().__init__(x, y, width, height, color)
        self.solid = solid  # True = can't jump through bottom, False = can
