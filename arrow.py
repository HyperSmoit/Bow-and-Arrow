from utils import *

class Arrow(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
        self.updateX = 0
        self.updateY = 0
        self.initialY = PLAYER_DIMENSIONS[1] // 2.75
        self.x = pos[0]
        self.y = pos[1]
        self.update_speed = 0
        self.current_speed = ARROW_INITIAL_SPEED
        self.launched = False
        self.angle = 0
    
    def draw(self, surf):
        self.image = pygame.transform.scale(pygame.image.load("arrow.png").convert_alpha(), ARROW_DIMENSIONS)
        # self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        # if self.launched == True:
        #     surf.blit(self.image, self.pos)
        # else:
        old_center = tuple(sum(x) for x in zip(self.rect.center, (self.x, self.y)))
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center = self.image.get_rect().center)
        new_rect.center = old_center
        surf.blit(rotated_image, new_rect) 

    def update(self, playerY):
        if self.launched == False:
            mouse_pos = pygame.mouse.get_pos()
            rel_x, rel_y = mouse_pos[0], mouse_pos[1] - self.y
            self.angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            if (self.y + self.updateY >= self.initialY) and (self.y + self.updateY <= HEIGHT - PLAYER_DIMENSIONS[1] + self.initialY):
                self.y += self.updateY
                self.rect.move_ip(0, self.y)
                self.pos[1] = self.y
            if self.current_speed < ARROW_MAX_SPEED:
                self.current_speed += self.update_speed
            else:
                self.current_speed = ARROW_INITIAL_SPEED
        else:
            self.updateX = self.current_speed * math.cos(math.radians(self.angle))
            self.updateY = self.current_speed * math.sin(math.radians(-self.angle))
            self.x += self.updateX
            self.y += self.updateY
            self.rect.move_ip(self.x, self.y)
            self.pos[0] = self.x
            self.pos[1] = self.y
            if self.x + WIDTH // 20 > WIDTH or self.y < 0 or self.y > HEIGHT:
                self.launched = False
                self.updateX = 0
                self.updateY = 0
                self.update_speed = 0
                self.x = PLAYER_DIMENSIONS[0] // 2.17
                self.y = playerY + self.initialY

    def collisionArrow(self, other):
        # Collision with another object
        width, height = pygame.Surface.get_size(other.image)
        if self.pos[0] + WIDTH // 20 > (other.pos[0] - 1) and self.pos[0] + WIDTH // 20 < (other.pos[0] + width + 1):
            if self.pos[1] > (other.pos[1] - 1) and self.pos[1] < (other.pos[0] + height + 1):
                print('collision', other)
                return True
        return False