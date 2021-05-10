from utils import pygame, SHURIKEN_DIMENSIONS, SHURIKEN_SPEED, HEIGHT, WIDTH
from pygame.locals import *
import random

class Shuriken(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
    
    def draw(self, surf):
        # Draw shuriken
        self.image = pygame.transform.scale(pygame.image.load("shuriken.png"), SHURIKEN_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        surf.blit(self.image, self.pos)

    def update(self):
        # Move to the left
        self.pos[0] -= SHURIKEN_SPEED
        self.rect.move_ip(self.pos[0], 0)
        if self.pos[0] < 0:
            self.refresh()

    def refresh(self):
        self.pos = [(random.uniform(2.6, 6.7)) * WIDTH / 2, random.randint(0, HEIGHT)]
