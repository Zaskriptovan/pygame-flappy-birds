import pygame

from settings import FPS
from rendering import Renderer, bird

pygame.init()
clock = pygame.time.Clock()

renderer = Renderer()

click = False
while True:
    # Управление
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN and click is False:
            if event.key == pygame.K_SPACE:
                click = True
                renderer.state = 'play'
                bird.speed_y = -14
        else:
            click = False

    # Обработка
    renderer.game_stage()
    renderer.background_spawn()
    renderer.background_movement()
    renderer.pipe_spawn()
    renderer.pipe_movement()
    renderer.collisions()
    renderer.update_score()

    # Отрисовка
    renderer.draw_background()
    renderer.draw_bird()
    renderer.draw_pipes()
    renderer.draw_score()

    pygame.display.update()
    clock.tick(FPS)
