#!/usr/bin/env python3

from utils import *
from balloon import *
from shuriken import *
from archer import *
from arrow import *
from cloud import *


pygame.init()
frame_rate = pygame.time.Clock()

class Game:

    def __init__(self):

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))

        # Add the game objects
        self.gameObjects = []
        self.player = Player([0,1])
        self.gameObjects.append(self.player)
        self.score = 0

        # Add the shurikens and generate their initial position
        for _ in range (0, 20):
            pos = [(random.uniform(2.6, 6.7)) * WIDTH / 2,random.randint(0, HEIGHT)]
            self.shuriken = Shuriken(pos)
            self.gameObjects.append(self.shuriken)

        # Add the balloons and generate their initial position
        for _ in range (0, 20):
            pos = [random.uniform(WIDTH / 3, WIDTH), random.uniform(5 * HEIGHT, HEIGHT)]
            self.balloon = Balloon(pos)
            self.gameObjects.append(self.balloon)
        
        # Add the clouds and generate their initial position
        for _ in range (0, 20):
            pos = [random.uniform(WIDTH / 5, WIDTH), random.uniform(7 * HEIGHT, HEIGHT)]
            self.cloud = Cloud(pos)
            self.gameObjects.append(self.cloud)

        # Add the arrow
        self.arrow = Arrow([PLAYER_DIMENSIONS[0] // 2.17, PLAYER_DIMENSIONS[1] // 2.75])
        self.gameObjects.append(self.arrow)

    def run(self):
        # Game stops when there are no lives left
        while self.gameObjects[0].life > 0:
            self.draw()
            self.input()
            self.update()
        while True:
            self.final()
            self.input()
        
    def collisionDetection(self):
        # Collision detection
        listshuriken = [x for x in self.gameObjects if isinstance(x, Shuriken)]
        listballoon = [x for x in self.gameObjects if isinstance(x, Balloon)]
        listcloud = [x for x in self.gameObjects if isinstance(x, Cloud)]
        for x in listshuriken:
            # Collision with archer
            if self.gameObjects[0].collisionArcher(x):
                self.gameObjects[0].oncollisionArcher()
                self.gameObjects.remove(x)
            # Collision with arrow
            if self.gameObjects[-1].collisionArrow(x):
                self.score += SHURIKEN_POINTS
                self.gameObjects.remove(x)
        for x in listballoon:
            # Collision with arrow
            if self.gameObjects[-1].collisionArrow(x):
                self.score += BALLON_POINTS
                self.gameObjects.remove(x)
        for x in listcloud:
            #  Collision with arrow
            if self.gameObjects[-1].collisionArrow(x):
                self.score -= CLOUD_POINTS
                self.gameObjects.remove(x)
                
        
    def update(self):
        self.collisionDetection()
        for i in range(0, len(self.gameObjects) - 1):
            self.gameObjects[i].update()
        self.gameObjects[-1].update(self.player.y)

    def input(self):
        # variable to check if the first arrow has been launched
        # has_been_pressed = 0
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
                # has_been_pressed = 1
                if self.arrow.launched == False:
                    self.arrow.update_speed += SPEED_INCREASE
                
            if event.type == MOUSEBUTTONUP:
                if self.arrow.launched == False:
                    self.arrow.launched = True
                # self.arrow.updateX = self.arrow.current_speed
                # self.arrow.pos = [PLAYER_DIMENSIONS[0] // 2.17, PLAYER_DIMENSIONS[1] // 2.75]
                # self.arrow.update_speed = 0
                # self.arrow.current_speed = ARROW_INITIAL_SPEED
                # print(self.arrow.updateX)
            # if event.type == MOUSEBUTTONUP:
            #     if event.type == MOUSEBUTTONDOWN:
            #        self.arrow.update_speed = 0
            #        self.arrow.updateX = 0
            #        self.arrow.updateY = 0                

    def draw(self):
        self.window.fill(BACKGROUND_COLOR)

        # Draw the score
        myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
        label1=myfont1.render("Score " + str(self.score), 1, (255,255,255))
        self.window.blit(label1,(WIDTH//2, 10))

        for gameObject in self.gameObjects:
            gameObject.draw(self.window)
            # self.window.blit(gameObject.image, gameObject.pos)
        pygame.display.update()
        frame_rate.tick(60)
    
    def final(self):
        self.window.fill(BACKGROUND_COLOR)

        myfont2 = pygame.font.SysFont("Comic Sans MS", 100)
        label2=myfont2.render("GAME OVER", 1, (0,0,0))
        self.window.blit(label2,(WIDTH - 500, HEIGHT - 100))

        myfont3 = pygame.font.SysFont("Comic Sans MS", 80)
        label3=myfont3.render("Score " + str(self.score), 1, (255,255,255))
        self.window.blit(label3,(WIDTH // 2 - 100, HEIGHT // 2 - 100))
        pygame.display.update()


def main():
    """
    Main function
    """
    game = Game()
    game.run()

main()
