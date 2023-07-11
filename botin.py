import pygame
from constantes import *
from auxiliar import Auxiliar
from modo import *


class Botin:
    def __init__(self, x, y, width, height, path, type):
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.type = type
        self.collition_rect = pygame.Rect(x+self.rect.width/10,y,self.rect.width/2,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        self.pizza_sound = pygame.mixer.Sound("images\music\pizza_soundeffect.wav")
    
    def update(self, player):
        if self.rect.colliderect(player.ground_collition_rect):
            self.rect.x = -1000
            self.collition_rect.x = -1000
            self.ground_collition_rect.x =-1000
            self.pizza_sound.play()
            if self.type == 1:                
                player.score += 100
            if self.type == 2:                
                player.score += 300
            elif self.type == 3:
                player.lives += 1 

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        if get_mode() :
            pygame.draw.rect(screen, color=(255, 0, 0), rect=self.collition_rect)
            pygame.draw.rect(screen, color=(255, 255, 0), rect=self.ground_collition_rect)

  