import pygame

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PIPE_WIDTH = 52
PIPE_LENGTH = 400
FPS = 60

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

font = pygame.font.SysFont('Comic Sans MS', 34, bold=True)

img_background = pygame.image.load('images/background.png').convert_alpha()
birds = pygame.image.load('images/bird.png').convert_alpha()
img_pipe_top = pygame.image.load('images/pipe_top.png').convert_alpha()
img_pipe_bottom = pygame.image.load('images/pipe_bottom.png').convert_alpha()
