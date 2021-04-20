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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                if event.key == K_w:
                    self.player.moveUp()
                if event.key == K_s:
                    self.player.moveDown()
            # if event.type == MOUSEMOTION:
            #     mouseX, mouseY = event.pos
            #     rel_x, rel_y = mouseX, mouseY - self.player.y
            #     angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            #     self.player.rotate(angle)
                

                

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
    # TODO 1.3
    game = Game()
    game.run()

main()
