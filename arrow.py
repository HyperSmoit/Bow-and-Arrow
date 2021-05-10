from utils import *

class Arrow(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
        self.updateX = 0
        self.updateY = 0
        self.x = pos[0]
        self.y = pos[1]
        self.update_speed = 0
        self.current_speed = ARROW_INITIAL_SPEED
    
    def draw(self):
        self.image = pygame.transform.scale(pygame.image.load("arrow.png").convert_alpha(), ARROW_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect() 

    def update(self):
        self.x += self.updateX
        self.y += self.updateY
        self.rect.move_ip(self.x, self.y)
        self.pos[0] = self.x
        self.pos[1] = self.y
        if self.current_speed < ARROW_MAX_SPEED:
            self.current_speed += self.update_speed
        else:
            self.current_speed = ARROW_INITIAL_SPEED

    def rotate(self):
        # TODO
        pass
        

    def collisionArrow(self, other):
        # Collision with another object
        width, height = pygame.Surface.get_size(other.image)
        if self.pos[0] > (other.pos[0] - 1) and self.pos[0] < (other.pos[0] + width + 1):
            if self.pos[1] > (other.pos[1] - 1) and self.pos[1] < (other.pos[0] + height + 1):
                return True
        return False
