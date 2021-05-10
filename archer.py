from utils import pygame, PLAYER_DIMENSIONS, PLAYER_VELOCITY, HEIGHT, math
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
        self.updateY = 0
        self.y = 0
        self.faceVector = [1,0]
        self.life = 3

    def draw(self):
        self.image = pygame.transform.scale(pygame.image.load("cupid.png").convert_alpha(), PLAYER_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
      
    # TODO
    def update(self):
        # mouse_pos = pygame.mouse.get_pos()
        # rel_x, rel_y = mouse_pos[0], HEIGHT - mouse_pos[1] - self.y
        # angle = math.degrees(math.atan2(rel_y, rel_x))
        # self.rotate(angle)
        self.y += self.updateY
        self.rect.move_ip(0, self.y)
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0
        self.pos[1] = self.y

        
    def rotate(self, angle):
        # TODO:
        # print(angle)
        # Rotate the image.
        # Update the rect and keep the center at the old position.
        rotated_image = pygame.transform.rotate(self.image, angle)
        new_rect = rotated_image.get_rect(center = self.image.get_rect().center)
        # surf.blit(rotated_image, new_rect)
        print(self.rect)
        self.image = rotated_image
        self.rect = new_rect
        print(self.rect)
        print()

    def collisionArcher(self, other):
        # Collision with another object
        width, height = pygame.Surface.get_size(self.image)
        print(width, height)
        if other.pos[0] < width:
            if other.pos[1] > self.pos[1] and other.pos[1] < self.pos[1] + height:
                return True 
        return False
    
    def oncollisionArcher(self):
        # Lose a life on collision
        self.life -= 1