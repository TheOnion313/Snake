import pygame
from random import randint as r
import main

apple = pygame.transform.scale(pygame.image.load('apple.png'), (main.SNAKE_SIZE, main.SNAKE_SIZE))


class Apple(object):

    def __init__(self):
        self.x = r(0, main.ROW_LENGTH) * main.SNAKE_SIZE
        self.y = r(0, main.COL_LENGTH) * main.SNAKE_SIZE

    def show(self):
        main.screen.blit(apple, (self.x, self.y))
