import pygame
import asyncio
from core.constants import WIDTH, HEIGHT, WHITE, FPS
from core.game_state_manager import GameStateManager


async def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jump Guy with Platforms")
    clock = pygame.time.Clock()

    state_manager = GameStateManager(screen)
    running = True

    while running:
        clock.tick(FPS)
        running = state_manager.handle_events()
        state_manager.update()
        state_manager.render()

        await asyncio.sleep(0)


asyncio.run(main())