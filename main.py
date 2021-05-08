#!/usr/bin/env python3

from utils import *
from balloon import *
from shuriken import *
from archer import *
from arrow import *

pygame.init()
frame_rate = pygame.time.Clock()

class Game:

    def __init__(self):

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.gameObjects = []
        self.player = Player([0,1])
        self.gameObjects.append(self.player)

        for i in range (0, 20):
            pos = [(random.uniform(2.6, 6.7)) * WIDTH / 2,random.randint(0, HEIGHT)]
            self.shuriken = Shuriken(pos)
            self.gameObjects.append(self.shuriken)

        for i in range (0, 20):
            pos = [random.uniform(WIDTH / 3, WIDTH), random.uniform(5 * HEIGHT, HEIGHT)]
            self.balloon = Balloon(pos)
            self.gameObjects.append(self.balloon)
        
        self.arrow = Arrow([PLAYER_DIMENSIONS[0] // 2.17, PLAYER_DIMENSIONS[1] // 2.75])
        self.gameObjects.append(self.arrow)

    def run(self):
        while True:
            self.draw()
            self.input()
            self.update()
            

    def collisionDetection(self):
        pass

    def update(self):
        for gameObject in self.gameObjects:
            gameObject.update()

    def input(self):
        has_been_pressed = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                if event.key == K_w:
                    self.player.updateY = -PLAYER_VELOCITY
                    self.arrow.updateY = -PLAYER_VELOCITY
                if event.key == K_s:
                    self.player.updateY = PLAYER_VELOCITY
                    self.arrow.updateY = PLAYER_VELOCITY
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    self.player.updateY = 0
                    self.arrow.updateY = 0
            if event.type == MOUSEBUTTONDOWN:
                # Add arrow speed
                has_been_pressed = 1
                self.arrow.update_speed += SPEED_INCREASE
                if event.type == MOUSEBUTTONUP:
                   self.arrow.updateX = 0
                   self.arrow.pos = [PLAYER_DIMENSIONS[0] // 2.17, PLAYER_DIMENSIONS[1] // 2.75]
            if event.type == MOUSEBUTTONUP:
                # Release arrow
                if event.type == MOUSEBUTTONDOWN:
                   self.arrow.update_speed = 0
                
                has_been_pressed = 0

                    
            # if event.type == MOUSEMOTION:
            #     mouseX, mouseY = event.pos
            #     # print(mouseX, mouseY)
            #     rel_x, rel_y = mouseX, mouseY - self.player.y
            #     angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            #     self.player.rotate(self.window, angle)
                

                

    def draw(self):
        self.window.fill(BACKGROUND_COLOR)
        for gameObject in self.gameObjects:
            gameObject.draw()
            self.window.blit(gameObject.image, gameObject.pos)
        pygame.display.update()
        frame_rate.tick(60)

def main():
    """Funcția main.

    """
    game = Game()
    game.run()

main()
