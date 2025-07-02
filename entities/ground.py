import pygame

GROUND_COLOR = (0, 150, 0)

class Ground:
    def __init__(self, y, height=50, color=GROUND_COLOR):
        self.y = y
        self.height = height
        self.color = color

    def draw(self, surface, screen_width):
        pygame.draw.rect(surface, self.color, (0, self.y, screen_width, self.height))

    def get_top(self):
        return self.y
