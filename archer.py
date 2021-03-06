from utils import pygame, PLAYER_DIMENSIONS, PLAYER_VELOCITY, HEIGHT, math, WIDTH
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
        self.updateY = 0
        self.y = 0
        self.life = 3
        self.angle = 0

    def draw(self, surf):
        self.image = pygame.transform.scale(pygame.image.load("cupid.png").convert_alpha(), PLAYER_DIMENSIONS)
        self.rect = self.image.get_rect()
        # Rotate initial image, then draw the obtained rotated image using blit
        old_center = tuple(sum(x) for x in zip(self.rect.center, (0, self.y)))
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center = self.image.get_rect().center)
        new_rect.center = old_center
        surf.blit(rotated_image, new_rect)
        # Draw lives
        myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
        label1 = myfont1.render("Lives: " + str(self.life), 1, (255, 255, 255))
        surf.blit(label1,(WIDTH // 2 + 1, 30))
      
    def update(self):
        # Update coordinates and angle
        mouse_pos = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_pos[0], mouse_pos[1] - self.y
        self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)        
        if (self.y + self.updateY >= 0) and (self.y + self.updateY <= HEIGHT - self.rect.height):
            self.y += self.updateY
            self.rect.move_ip(0, self.y)
            self.pos[1] = self.y

    def collisionArcher(self, other):
        # Collision with another object
        width, height = pygame.Surface.get_size(self.image)
        if other.pos[0] < width:
            if other.pos[1] > self.pos[1] and other.pos[1] < self.pos[1] + height:
                return True 
        return False
    
    def oncollisionArcher(self):
        # Lose a life on collision
        self.life -= 1