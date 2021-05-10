from utils import *
from pygame.locals import *


class Cloud(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
    
    def draw(self):
        self.image = pygame.transform.scale(pygame.image.load("cloud.png").convert(), CLOUD_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        # Move up
        self.pos[1] -= CLOUD_SPEED
        self.rect.move_ip(0, self.pos[1])

    def collision(self, other):
        pass
