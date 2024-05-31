import pygame


class Cube:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("cube.png")
        self.image_size = self.image.get_size()
        self.delta = .1



