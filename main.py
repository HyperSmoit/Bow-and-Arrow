#!/usr/bin/env python3

import random
import pygame, sys
from pygame.locals import *
import argparse

pygame.init()
frame_rate = pygame.time.Clock()

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
PAD_VELOCITY = 9
INITIAL_LEFT_POSITION = [HALF_PAD_WIDTH - 1, HEIGHT // 2]
INITIAL_RIGHT_POSITION = [WIDTH + 1 - HALF_PAD_WIDTH, HEIGHT // 2]


class GameObject:
    def __init__(self, game, position, velocity, dimensions):
        self.position = position
        self.game = game
        self.velocity = velocity
        self.dimensions = dimensions

    def draw(self):
        pass

    def update(self):
        pass

    def collidesWith(self, other):
        """Funcție care determină starea de coliziune între obiectele self și other.

        Args:
            self: obiectul self.
            other: obiectul pentru care se testează coliziunea.

        Returns: 
            true/false.
        """
        
        # TODO 5
        print("PLATFORM =   {}",other.position[1] - other.dimensions[1] / 2)
        print("BALL =   {}",self.position[1] - self.dimensions[1] / 2)
        if (self.position[1]<= other.position[1] + other.dimensions[1])and (self.position[1] >= other.position[1] - other.dimensions[1]): # Y axis check
            if self.position[0] < WIDTH/2:
                if (self.position[0] - self.dimensions[0] >= other.position[0]) and (self.position[0] - self.dimensions[0] <= other.position[0] + other.dimensions[0]): # X axis check
                    return True
            else:
                if (self.position[0] + self.dimensions[0] <= other.position[0]) and (self.position[0] + self.dimensions[0] >= other.position[0] - other.dimensions[0]) / 2: # X axis check
                    return True
        return False


class Paddle(GameObject):
    def __init__(self, game, position, dimensions):
        super().__init__(game, position, [0, 0], dimensions)

    def draw(self):
        pygame.draw.polygon(self.game.window, GREEN, [[self.position[0] - HALF_PAD_WIDTH, self.position[1] - HALF_PAD_HEIGHT], [self.position[0] - HALF_PAD_WIDTH, self.position[1] + HALF_PAD_HEIGHT], [self.position[0] + HALF_PAD_WIDTH, self.position[1] + HALF_PAD_HEIGHT], [self.position[0] + HALF_PAD_WIDTH, self.position[1] - HALF_PAD_HEIGHT]], 0)

    def update(self):
        self.position[1] += self.velocity[1]
        if self.position[1] + HALF_PAD_HEIGHT > HEIGHT:
            self.position[1] = HEIGHT - + HALF_PAD_HEIGHT
        if self.position[1] - HALF_PAD_HEIGHT < 0:
            self.position[1] = HALF_PAD_HEIGHT

    def moveUp(self):
        self.velocity[1] = -PAD_VELOCITY

    def moveDown(self):
        self.velocity[1] = PAD_VELOCITY

    def stop(self):
        self.velocity[1] = 0

class Ball(GameObject):

    def __init__(self, game, position, dimensions):
        velocity = [0, 0]
        self.up = 1
        while velocity[0] == 0 or velocity[1] == 0:
            velocity = [random.randrange(-1, 1), random.randrange(-1, 1)]
        super().__init__(game, position, velocity, dimensions)

    def draw(self):
        """Funcție care desenează mingea.

        Args:
            self: obiectul self.
        """
        # TODO 2.2
        pygame.draw.circle(self.game.window, RED, self.position, self.dimensions[0])

        pass

    def update(self):
        """Funcție care actualizează poziția mingii.

        Args:
            self: obiectul self.
        """
        # TODO 3.1
        self.position[0] += int(self.velocity[0])
        self.position[1] += int(self.velocity[1]) * self.up
        # TODO 3.2
        if self.position[1] + self.dimensions[1] > HEIGHT:
            self.up = 1
        if self.position[1] - self.dimensions[1] < 0:
            self.up = -1

        if self.position[0] - self.dimensions[0] < -10:
            self.reset()
            self.game.rightPlayerScore += 1
        if self.position[0] + self.dimensions[0] > WIDTH + 10:
            self.reset()
            self.game.leftPlayerScore += 1

    def reset(self):
        self.game.ball = Ball(self.game, [WIDTH // 2, HEIGHT // 2], [BALL_RADIUS, BALL_RADIUS])
        self.game.gameObjects.remove(self)
        self.game.gameObjects.append(self.game.ball)

    def onCollision(self, other):
        self.velocity[0] *= -1.4



class Game:

    def __init__(self):
        """Funcție care inițializează jocul.

        Args:
            self: obiectul self.
        """
        # TODO 1.1
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.gameObjects = []
        self.paddleLeft = None
        self.paddleRight = None
        self.ball = None

        # TODO 1.2
        # HINT: 
        #   Pentru poziția padelelor folosiți:
        #       INITIAL_LEFT_POSITION, INITIAL_RIGHT_POSITION
        #   Pentru dimensiunea unei padele folosiți:
        #       HALF_PAD_WIDTH, HALF_PAD_HEIGHT
        #   Pentru poziția mingii:
        #       WIDTH, HEIGHT
        #   Pentru dimensiunea mingii:
        #       BALL_RADIUS
        pygame.display.set_caption('Game')
        self.paddleLeft = Paddle(self, INITIAL_LEFT_POSITION, (HALF_PAD_WIDTH, HALF_PAD_HEIGHT))
        self.paddleRight = Paddle(self, INITIAL_RIGHT_POSITION, (HALF_PAD_WIDTH, HALF_PAD_HEIGHT))
        self.ball = Ball(self, [WIDTH/2, HEIGHT/2] , (BALL_RADIUS, BALL_RADIUS))

        self.gameObjects.append(self.paddleRight)
        self.gameObjects.append(self.paddleLeft)
        self.gameObjects.append(self.ball)

        self.leftPlayerScore = 0
        self.rightPlayerScore = 0

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()

    def collisionDetection(self):
        for target in self.gameObjects:
            if self.ball != target:
                if self.ball.collidesWith(target):
                    self.ball.onCollision(target)

    def update(self):
        self.collisionDetection()
        for gameObject in self.gameObjects:
            gameObject.update()

    def input(self):
        """Funcție care preia inputul de la tastatură.

        Args:
            self: obiectul self.
        """

        for event in pygame.event.get():
            if event.type == KEYUP:
                if event.key == K_UP:
                    self.paddleRight.stop()
                if event.key == K_DOWN:
                    self.paddleRight.stop()
                if event.key == K_w:
                    self.paddleLeft.stop()
                if event.key == K_s:
                    self.paddleLeft.stop()
            # TODO 4
            # HINT:
            #   Paddle.moveUp()
            #   Paddle.moveDown()
            if event.type == KEYDOWN:
                if event.key == K_w:
                    self.paddleLeft.moveUp()
                if event.key == K_s:
                    self.paddleLeft.moveDown()
                if event.key == K_UP:
                    self.paddleRight.moveUp()
                if event.key == K_DOWN:
                    self.paddleRight.moveDown()



    def draw(self):
        """Funcție care randează scena.

        Args:
            self: obiectul self.
        """

        # TODO 2.1.1
        # HINT:
        #   Colorați fundalul cu BLACK.
        self.window.fill(BLACK)
        pygame.draw.line(self.window, WHITE, [WIDTH // 2, 0],[WIDTH // 2, HEIGHT], 1)
        pygame.draw.line(self.window, WHITE, [PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1)
        pygame.draw.line(self.window, WHITE, [WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1)
        pygame.draw.circle(self.window, WHITE, [WIDTH // 2, HEIGHT//2], 70, 1)

        myfont1 = pygame.font.SysFont("Comic Sans MS", 20)
        label1 = myfont1.render("Score " + str(self.leftPlayerScore), 1, (255,255,0))
        self.window.blit(label1, (50,20))

        myfont2 = pygame.font.SysFont("Comic Sans MS", 20)
        label2 = myfont2.render("Score " + str(self.rightPlayerScore), 1, (255,255,0))
        self.window.blit(label2, (470, 20))

        # TODO 2.1.2
        # HINT:
        #   Desenați toate obiectele din self.gameObjects;
        #   Actualizați ecranul;
        #   Setați frame rate-ul la 60 FPS.
        for gameObject in self.gameObjects:
            gameObject.draw()
        pygame.display.update()
        frame_rate.tick(60)

def main():
    """Funcția main.

    """
    # TODO 1.3
    game = Game()
    game.run()

main()
