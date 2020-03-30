import pygame
import main


class SnakeUnit(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        pygame.draw.rect(main.screen, main.SNAKE_COLOR, (
        self.x + main.OUTLINE, self.y + main.OUTLINE, main.SNAKE_SIZE - main.OUTLINE, main.SNAKE_SIZE - main.OUTLINE))
