from utils import pygame, SHURIKEN_DIMENSIONS, SHURIKEN_SPEED
from pygame.locals import *

class Shuriken(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
    
    def draw(self):
        self.image = pygame.transform.scale(pygame.image.load("shuriken.png"), SHURIKEN_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        # Move to the left
        self.pos[0] -= SHURIKEN_SPEED
        self.rect.move_ip(self.pos[0], 0)
        
    def collision(self, other):
        pass
