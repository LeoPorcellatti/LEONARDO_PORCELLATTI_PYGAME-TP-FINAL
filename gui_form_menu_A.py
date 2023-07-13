import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_label import Label
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from background import Background


class FormMenuA(Form):
    
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images\gui\menu\sound.png")
        self.boton1 = Button(master=self,x=1650,y=410,w=140,h=180,color_background=None,color_border=None,image_background="images\gui\menu\home.png",on_click=self.on_click_boton1,on_click_param="form_menu_principal",text="",font="Verdana",font_size=30,font_color=C_WHITE)
        self.label = Label(master=self,x=600,y=400,w=600,h=50,color_background=None,color_border=None,image_background="images\gui\menu\label.png", text = "Label", font = "Arial", font_size=14, font_color=C_BLUE)               
        self.lista_widget = [self.boton1, self.label]
  
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

        
