import pygame

from models import Bird, Pipe, Score
from settings import screen, WINDOW_WIDTH, img_background, birds, img_pipe_top, img_pipe_bottom, WINDOW_HEIGHT

pygame.init()

bird = Bird()


class Renderer:
    def __init__(self):
        self.backgrounds = [pygame.Rect(0, 0, 288, 600)]
        self.frame = 0
        self.score = 0
        self.pipes = []
        self.pipes_score = []
        self.state = 'start'

    def draw_score(self):
        score_text = Score(self.score)
        screen.blit(score_text.text, (WINDOW_WIDTH // 2, 30))

    def draw_background(self):
        for bg in self.backgrounds:
            screen.blit(img_background, bg)

    def draw_bird(self):
        self.frame = (self.frame + 0.2) % 4
        img_bird = birds.subsurface(34 * int(self.frame), 0, 34, 24)
        if self.state == 'play':
            img_bird = pygame.transform.rotate(img_bird, -bird.speed_y * 3)
        screen.blit(img_bird, bird.model)

    def draw_pipes(self):
        for pipe in self.pipes:
            if pipe.y == 0:
                rect = img_pipe_top.get_rect(bottomleft=pipe.bottomleft)
                screen.blit(img_pipe_top, rect)
            else:
                rect = img_pipe_bottom.get_rect(topleft=pipe.topleft)
                screen.blit(img_pipe_bottom, rect)

    def update_score(self):
        for pipe in self.pipes:
            if pipe.right < bird.model.left and pipe not in self.pipes_score:
                self.pipes_score.append(pipe)
                self.score += 0.5

    def collisions(self):
        for pipe in self.pipes:
            if bird.model.colliderect(pipe) or bird.model.top < 0 or bird.model.bottom > WINDOW_HEIGHT:
                self.state = 'start'
                self.score = 0

    def pipe_spawn(self):
        if self.state == 'play':
            if len(self.pipes) == 0 or self.pipes[-1].x < WINDOW_WIDTH - 200:
                pipe_texture = Pipe()
                self.pipes.append(pipe_texture.create_pipe_top())
                self.pipes.append(pipe_texture.create_pipe_bottom())

    def pipe_remove(self, pipe):
        if pipe.right < 0:
            self.pipes.remove(pipe)
            if pipe in self.pipes_score:
                self.pipes_score.remove(pipe)

    def pipe_movement(self):
        for pipe in reversed(self.pipes):
            pipe.x -= 5
            self.pipe_remove(pipe)

    def background_spawn(self):
        if self.backgrounds[-1].right <= WINDOW_WIDTH:
            self.backgrounds.append(pygame.Rect(self.backgrounds[-1].right, 0, 288, 600))

    def background_remove(self, bg):
        if bg.right < 0:
            self.backgrounds.remove(bg)

    def background_movement(self):
        for bg in reversed(self.backgrounds):
            bg.x -= 1
            self.background_remove(bg)

    def game_stage(self):
        if self.state == 'start':
            self.pipes = []
            bird.model.y = WINDOW_HEIGHT // 2
        elif self.state == 'play':
            bird.speed_y += 1
            bird.model.y += bird.speed_y
