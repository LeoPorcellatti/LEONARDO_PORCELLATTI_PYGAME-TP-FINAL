import pygame
from pygame.locals import *
from gui_form_menu_game_l1 import FormGameLevel1
from gui_form_menu_game_l2 import FormGameLevel2

class Manejador_niveles:
    def __init__(self, pantalla):
        self._slave = pantalla
        self.niveles = {"nivel_uno": FormGameLevel1, "nivel_dos": FormGameLevel2}

    def get_niveles(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave) # CONSTRUYE EL NIVEL 