import pygame
class Platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("platform.png")
        self.rescale_image()
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
    def rescale_image(self):
        self.image_size = self.image.get_size()
        scale_size = (int(self.image_size[0] * .1), int(self.image_size[1]*.1))
        self.image = pygame.transform.scale(self.image,scale_size)

