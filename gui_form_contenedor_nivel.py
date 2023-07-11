import pygame
from pygame.locals import *
import json
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_graph import Graph
from gui_label import Label
from background import Background
from constantes import *


class FormContenedorNiveles(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images\gui\menu\menu.png")
        self.boton1 = Button(master=self,x=760,y=320,w=140,h=50,color_background=None,color_border="Black",image_background="images\gui\menu\\buttons\Level1.png",on_click=self.on_click_boton1,on_click_param="form_game_L1",text="Nivel 1",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=910,y=320,w=140,h=50,color_background=None,color_border="Black",image_background="images\gui\menu\\buttons\Level2.png",on_click=self.on_click_boton2,on_click_param="form_game_L2",text="Nivel 2",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=830,y=380,w=140,h=50,color_background=None,color_border="Black",image_background="images\gui\menu\\buttons\Level3.png",on_click=self.on_click_boton3,on_click_param="form_game_L3",text="Nivel 3",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton4 = Button(master=self,x=830,y=110,w=140,h=180,color_background=None,color_border=None,image_background="images\gui\menu\home.png",on_click=self.on_click_boton4,on_click_param="form_menu_principal",text="",font="Verdana",font_size=30,font_color=C_WHITE)
                       
        self.lista_widget = [self.boton1,self.boton2,self.boton3, self.boton4]



    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        pygame.mixer.music.load("images/music/01-Level1.wav")   
        pygame.mixer.music.play()
    
    def on_click_boton2(self, parametro):
        self.set_active(parametro)
        pygame.mixer.music.load("images/music/02-Level2.wav")
        pygame.mixer.music.play()
    
    def on_click_boton3(self, parametro):
        self.set_active(parametro)
        pygame.mixer.music.load("images/music/03-Level3.wav")
        pygame.mixer.music.play()

    def on_click_boton4(self, parametro):
        self.set_active(parametro)
        pygame.mixer.music.load("images/music/00-Menu.wav")
        pygame.mixer.music.play()
       

    ######## ANDA ##############    
    '''
    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        if parametro == "form_game_L1":
            pygame.mixer.music.load("images/music/01-Level1.wav")
            
        elif parametro == "form_game_L2":
            pygame.mixer.music.load("images/music/02-Level2.wav")
            
        elif parametro == "form_game_L3":
            pygame.mixer.music.load("images/music/03-Level3.wav")

        elif parametro == "form_menu_principal":
            pygame.mixer.music.load("images/music/00-Menu.wav")
        pygame.mixer.music.play()
    
    '''
    



    # def on_click_boton2(self, parametro):
    #     self.graph1.x0 = int(self.txt_x0._text)
    #     self.graph1.x1 = int(self.txt_x1._text)
    #     self.graph1.y0 = int(self.txt_y0._text)
    #     self.graph1.y1 = int(self.txt_y1._text)
    #     self.calcular()

    # def on_click_boton3(self, parametro):
    #     self.graph1.x0 = int(self.txt_x0._text)
    #     self.graph1.x1 = int(self.txt_x1._text)
    #     self.graph1.y0 = int(self.txt_y0._text)
    #     self.graph1.y1 = int(self.txt_y1._text)
    # def on_click_boton4(self, parametro):
    #     pass

 
    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()

        
