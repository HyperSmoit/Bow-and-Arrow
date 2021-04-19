#!/usr/bin/env python3

import random
import pygame, sys, os
from pygame.locals import *
import argparse

pygame.init()
frame_rate = pygame.time.Clock()
BACKGROUND_COLOR = (95,158,160)
WIDTH = 1280
HEIGHT = 720
PLAYER_DIMENSIONS = (WIDTH // 10, HEIGHT // 4)
PLAYER_VELOCITY = 10


class Shuriken(pygame.sprite.Sprite):
    pass

class Balloons(pygame.sprite.Sprite):
    pass

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = None
        self.rect = Rect(0, 0, 0, 0)
        self.y = 0

    def draw(self):
        self.image = pygame.transform.scale(pygame.image.load("archer.png"), PLAYER_DIMENSIONS)
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect() 
      
    def update(self):
        self.rect.move_ip(0, self.y)
        print(self.rect.top)
        if self.rect.top > HEIGHT:
            self.rect.top = HEIGHT
        if self.rect.bottom < 0:
            self.rect.bottom = 0
    def moveUp(self):
        self.y += -PLAYER_VELOCITY

    def moveDown(self):
        self.y += PLAYER_VELOCITY

class Game:

    def __init__(self):

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.gameObjects = []
        self.player = Player()
        self.gameObjects.append(self.player)

    def run(self):
        while True:
            self.input()
            self.update()
            self.draw()

    def collisionDetection(self):
        pass

    def update(self):
        for gameObject in self.gameObjects:
            gameObject.update()

    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_w:
                    self.player.moveUp()
                if event.key == K_s:
                    self.player.moveDown()

    def draw(self):
        self.window.fill(BACKGROUND_COLOR)
        for gameObject in self.gameObjects:
            gameObject.draw()
        self.window.blit(self.player.image, [0,self.player.x])
        pygame.display.update()
        frame_rate.tick(60)

def main():
    """Funcția main.

    """
    # TODO 1.3
    game = Game()
    game.run()

main()
