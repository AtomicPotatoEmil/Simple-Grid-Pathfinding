import pygame

class Tile:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.collided = False
        self.rect = pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x, y, 50, 50), 1)

    def draw(self):
        self.rect = pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(self.x, self.y, 50, 50), 1)