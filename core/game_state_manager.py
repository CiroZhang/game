from entities.player import Player
from entities.game_platform import Platform
from entities.ground import Ground
from physics.physics import *
from core.constants import WIDTH, HEIGHT, GROUND_COLOR
import pygame

class GameStateManager:
    def __init__(self, screen):
        self.screen = screen
        self.ground = Ground(y=HEIGHT - 50)
        self.player = Player(x=100, y=self.ground.get_top() - 60)
        self.platforms = [
            Platform(200, 450, 150, solid=True),
            Platform(400, 350, 120, solid=True),
            Platform(600, 250, 100, solid=False),
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.player.jump()
        if keys[pygame.K_a]:
            self.player.move_left()
        if keys[pygame.K_d]:
            self.player.move_right()
        return True

    def update(self):
        apply_movement(self.player)
        apply_gravity(self.player)
        apply_collision(self.player, self.ground, self.platforms)

    def render(self):
        self.screen.fill((255, 255, 255))
        self.ground.draw(self.screen, WIDTH)
        for plat in self.platforms:
            plat.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
