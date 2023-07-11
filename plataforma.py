import pygame
from constantes import *
from auxiliar import Auxiliar
from modo import *


class Plataform:
    def __init__(self, x, y,width, height, path, speed, frame_rate_ms, move_rate_ms, type):
        # self.image = Auxiliar.getSurfaceFromSeparateFiles("images\platforms\plataforma_alcantarilla({0}).png",0,2)[type]
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect = pygame.Rect(self.rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.speed = speed
        self.type = type
        self.move_x = 0
        self.move_y = 0
        self.move_flag = False
        self.move = False
        self.frame_rate_ms = frame_rate_ms 
        self.move_rate_ms = move_rate_ms
    
    def change_x(self): 
        if self.type == 1 or self.type == 2:
            if self.rect.x < 1400 and self.move_flag == False:
                self.rect.x += self.speed
                self.collition_rect.x += self.speed
                self.ground_collition_rect.x += self.speed
            elif self.rect.x <= 1400 and self.move_flag == True:
                self.rect.x -= self.speed
                self.collition_rect.x -= self.speed
                self.ground_collition_rect.x -= self.speed
        else:
            if self.rect.x < 1700 and self.move_flag == False:
                self.rect.x += self.speed
                self.collition_rect.x += self.speed
                self.ground_collition_rect.x += self.speed
            elif self.rect.x <= 1700 and self.move_flag == True:
                self.rect.x -= self.speed
                self.collition_rect.x -= self.speed
                self.ground_collition_rect.x -= self.speed
    

    
    # def change_y(self): 
    #     if self.rect.y >= 250 and self.move_flag == True:
    #         self.rect.y += self.speed
    #         self.collition_rect.y += self.speed
    #         self.ground_collition_rect.y += self.speed
    #     elif self.rect.y <= 500 and self.move_flag == False:
    #         self.rect.y -= self.speed
    #         self.collition_rect.y -= self.speed
    #         self.ground_collition_rect.y -= self.speed 
        

    def do_movement(self):
        if self.speed > 0:
            self.move = True
            if self.type == 1 and self.move:
                    self.change_x()                
                    if self.rect.x >= 900:
                        self.move_flag = True
                    elif self.rect.x <= 500:
                        self.move_flag = False
            elif self.type == 2 and self.move:
                    self.change_x()                
                    if self.rect.x >= 500:
                        self.move_flag = True
                    elif self.rect.x <= 200:
                        self.move_flag = False
            elif self.type == 3 and self.move:
                    self.change_x()                
                    if self.rect.x >= 1700:
                        self.move_flag = True
                    elif self.rect.x <= 1400:
                        self.move_flag = False
            # elif self.type == 2 and self.move:
            #     self.change_y()
            #     if self.rect.y <= 250:
            #         self.move_flag = True
            #     elif self.rect.y >= 500:
            #         self.move_flag = False  

   
    def update(self):
        self.do_movement()  

    def draw(self,screen):
        screen.blit(self.image,self.rect)
        if get_mode():
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        