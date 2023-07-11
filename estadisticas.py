import pygame
from constantes import *
from auxiliar import Auxiliar

class Estadistica:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fuente = pygame.font.Font("images\\gui\\fonts\\Turtles.otf",40)
        self.contador_segundos = pygame.time.get_ticks()  
        self.tiempo_limite = 300000


    def draw(self, screen):
        delta_time = pygame.time.get_ticks() - self.contador_segundos  
        tiempo_restante = max(0, self.tiempo_limite - delta_time)
        tiempo_restante_segundos = int(tiempo_restante/1000)
        tiempo_restante = str(tiempo_restante_segundos)
        contador = self.fuente.render("Tiempo: " + tiempo_restante, 0, (GREEN_TURTLE))
        screen.blit(contador,(750,10))
            
        

