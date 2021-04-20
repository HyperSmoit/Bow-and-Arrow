#!/usr/bin/env python3

import random
import pygame, sys, os
from pygame.locals import *
import argparse
import math

pygame.init()
frame_rate = pygame.time.Clock()
BACKGROUND_COLOR = (95,158,160)
WIDTH = 1280
HEIGHT = 720
PLAYER_DIMENSIONS = (WIDTH // 10, HEIGHT // 4)
PLAYER_VELOCITY = 10
SHURIKEN_DIMENSIONS = (WIDTH // 30, HEIGHT // 10)
SHURIKEN_SPEED = 7
BALLOON_SPEED = 2
BALLOON_DIMENSIONS = (WIDTH // 20, HEIGHT // 7)

class Shuriken(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
    
    def draw(self):
        self.image = pygame.transform.scale(pygame.image.load("shuriken.png"), SHURIKEN_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        self.pos[0] -= SHURIKEN_SPEED
        self.rect.move_ip(self.pos[0], 0)
        
    def collision(self, other):
        pass

class Balloon(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
    
    def draw(self):
        self.image = pygame.transform.scale(pygame.image.load("balloon.png").convert(), BALLOON_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

    def update(self):
        self.pos[1] -= BALLOON_SPEED
        self.rect.move_ip(0, self.pos[1])

    def collision(self, other):
        pass

class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = []
    
    def draw(self):
        pass

    def update(self):
        pass

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.pos = pos
        self.y = 0
        self.faceVector = [1,0]

    def draw(self):
        self.image = pygame.transform.scale(pygame.image.load("archer.png").convert_alpha(), PLAYER_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect() 
      
    def update(self):
        self.rotate()
        self.rect.move_ip(0, self.y)
        if self.rect.top > HEIGHT:
            self.rect.top = HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0
        self.pos[1] = self.y
        
    def moveUp(self):
        self.y += -PLAYER_VELOCITY

    def moveDown(self):
        self.y += PLAYER_VELOCITY
    def rotate(self):
        mouse_pos = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_pos[0], mouse_pos[1] - self.y
        angle = -math.degrees(math.atan2(rel_y, rel_x))
        # Rotate the image.
        self.image = pygame.transform.rotozoom(self.image, angle, 1)
        # Update the rect and keep the center at the old position.
        self.rect = self.image.get_rect(center=self.rect.center)


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
