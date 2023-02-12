from random import randint

import pygame

from settings import WINDOW_WIDTH, WINDOW_HEIGHT, PIPE_WIDTH, PIPE_LENGTH, font

pygame.init()


class Bird:
    def __init__(self):
        self.y = WINDOW_HEIGHT // 2
        self.speed_y = 0
        self.model = pygame.Rect(WINDOW_WIDTH // 3, self.y, 34, 24)


class Pipe:
    def __init__(self):
        self.pipe_differ = randint(100, 300)

    def create_pipe_top(self):
        pipe_top = pygame.Rect((WINDOW_WIDTH, 0), (PIPE_WIDTH, PIPE_LENGTH - self.pipe_differ))
        return pipe_top

    def create_pipe_bottom(self):
        pipe_bottom = pygame.Rect((WINDOW_WIDTH, WINDOW_HEIGHT - self.pipe_differ), (PIPE_WIDTH, PIPE_LENGTH))
        return pipe_bottom


class Score:
    def __init__(self, score):
        self.text = font.render(str(int(score)), True, 'white')
