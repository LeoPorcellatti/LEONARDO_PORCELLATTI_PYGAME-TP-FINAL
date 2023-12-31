import pygame
from constantes import *
from auxiliar import Auxiliar


class Cronometro:
    def __init__(self, x, y, tiempo_limite):
        self.x = x
        self.y = y
        self.fuente = pygame.font.Font("images\\gui\\fonts\\Turtles.otf",40)
        self.contador_segundos = pygame.time.get_ticks()  
        self.tiempo_limite = tiempo_limite
        self.time_out = False
        
    def draw(self, screen):
        delta_time = pygame.time.get_ticks() - self.contador_segundos  
        tiempo_restante = max(0, self.tiempo_limite - delta_time)
        tiempo_restante_segundos = int(tiempo_restante/1000)
        tiempo_restante = str(tiempo_restante_segundos)        
        contador = self.fuente.render("Tiempo: " + tiempo_restante, 0, (GREEN_TURTLE))
        screen.blit(contador,(750,10))
        if tiempo_restante_segundos == 0:
            self.time_out = True

