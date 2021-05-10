from utils import pygame, BALLOON_DIMENSIONS, BALLOON_SPEED
from pygame.locals import *


class Balloon(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
    
    def draw(self, surf):
        self.image = pygame.transform.scale(pygame.image.load("balloon.png").convert(), BALLOON_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        surf.blit(self.image, self.pos)

    def update(self):
        # Move up
        self.pos[1] -= BALLOON_SPEED
        self.rect.move_ip(0, self.pos[1])

    def collision(self, other):
        pass
