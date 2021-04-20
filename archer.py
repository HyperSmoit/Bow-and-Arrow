from utils import pygame, PLAYER_DIMENSIONS, PLAYER_VELOCITY, HEIGHT, math
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
        self.y = 0
        self.faceVector = [1,0]

    def draw(self):
        self.image = pygame.transform.scale(pygame.image.load("archer.png").convert_alpha(), PLAYER_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect() 
      
    def update(self):
        self.rotate()
        self.rect.move_ip(0, self.y)
        if self.rect.top > HEIGHT:
            self.rect.top = HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0
        self.pos[1] = self.y
        
    def moveUp(self):
        self.y += -PLAYER_VELOCITY

    def moveDown(self):
        self.y += PLAYER_VELOCITY
    def rotate(self):
        mouse_pos = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_pos[0], mouse_pos[1] - self.y
        angle = -math.degrees(math.atan2(rel_y, rel_x))
        # Rotate the image.
        self.image = pygame.transform.rotozoom(self.image, angle, 1)
        # Update the rect and keep the center at the old position.
        self.rect = self.image.get_rect(center=self.rect.center)

