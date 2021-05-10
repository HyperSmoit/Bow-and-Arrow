from utils import pygame, BALLOON_DIMENSIONS, BALLOON_SPEED, HEIGHT, WIDTH
from pygame.locals import *
import random

class Balloon(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
    
    def draw(self, surf):
        # Draw balloon
        self.image = pygame.transform.scale(pygame.image.load("balloon.png").convert(), BALLOON_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        surf.blit(self.image, self.pos)

    def update(self):
        # Move up
        self.pos[1] -= BALLOON_SPEED
        self.rect.move_ip(0, self.pos[1])
        if self.pos[1] < -self.rect.bottom:
            self.refresh()

    def refresh(self):
            self.pos = [random.uniform(WIDTH / 3, WIDTH), random.uniform(5 * HEIGHT, HEIGHT)]
