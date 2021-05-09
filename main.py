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
        self.score = 0

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
        while self.gameObjects[0].life > 0:#jocul se opreste cand raman fara vieti
            self.draw()
            self.input()
            self.update()
        while True:
            self.final()
            self.input()
        
            

    def collisionDetection(self):
        listshuriken=[x for x in self.gameObjects if isinstance(x,Shuriken)]
        listballoon=[x for x in self.gameObjects if isinstance(x,Balloon)]
        for x in listshuriken:
            if self.gameObjects[0].collisionArcher(x):
                self.gameObjects[0].oncollisionArher()
                self.gameObjects.remove(x)
        for x in listballoon:
            if self.gameObjects[-1].collisionArrow(x):
                self.score += 20
                self.gameObjects.remove(x)
        
    def update(self):
        self.collisionDetection()
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

        myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
        label1=myfont1.render("Score " + str(self.score), 1, (255,255,255))
        self.window.blit(label1,(WIDTH//2, 10))

        for gameObject in self.gameObjects:
            gameObject.draw()
            self.window.blit(gameObject.image, gameObject.pos)
        pygame.display.update()
        frame_rate.tick(60)
    
    def final(self):
        self.window.fill(BACKGROUND_COLOR)

        myfont2 = pygame.font.SysFont("Comic Sans MS", 100)
        label2=myfont2.render("GAME OVER", 1, (0,0,0))
        self.window.blit(label2,(WIDTH - 500, HEIGHT - 100))

        myfont3 = pygame.font.SysFont("Comic Sans MS", 80)
        label3=myfont3.render("Score " + str(self.score), 1, (255,255,255))
        self.window.blit(label3,(WIDTH//2-100,HEIGHT//2-100))
        pygame.display.update()


def main():
    """Funcția main.

    """
    game = Game()
    game.run()

main()
