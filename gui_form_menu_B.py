import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from background import Background
from constantes import *
from gui_label import Label
import sqlite3


class FormMenuB(Form):
    def __init__(self, name, master_surface, x, y, w, h, color_background, color_border, active, score, margen_y, margen_x, espacio):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images\gui\menu\\ranking.png")
        self._slave = self.static_background 
        #self._score = FormMenuPrincipal.get_score()
        self.borrar = score
        self._margen_y = margen_y

        self.boton1 = Button(master=self,x=830,y=400,w=70,h=110,color_background=None,color_border=None,image_background="images\gui\menu\home.png",on_click=self.on_click_boton1,on_click_param="form_menu_principal",text="",font="Verdana",font_size=30,font_color=C_WHITE)
        self.lbl_jugador = Label(master=self, x=400, y=100 , w= 200, h=200, text="PLAYER", font="Year supply of fairy cakes", font_size=40, font_color="Dark Red", image_background="images\\gui\\menu\\banner.png", color_background=None, color_border=None)
        self.lbl_puntaje = Label(master=self, x=1200, y=100 , w= 200, h=200, text="SCORE", font="Year supply of fairy cakes", font_size=40, font_color="Dark Red", image_background="images\\gui\\menu\\banner.png", color_background=None, color_border=None)
        self.lista_widget = [self.boton1, self.lbl_jugador, self.lbl_puntaje]
        
        # inicial_y = margen_y
        # for e in self._score:
        #     inicial_x = margen_x
        #     for n, s in e.items():
        #         cadena = ""
        #         cadena = f"{s}"
        #         jugador = Label(master=self, x=inicial_x, y=inicial_y, w=200, h= 100, text=cadena, font = "verdana", font_size = 30, font_color="White")
        #         self.lista_widget.append(jugador)
        #         inicial_x += w/2 - margen_x
        #     inicial_y += 100 + espacio
           

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def crear_datos_ranking(self):
        import sqlite3
        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                conexion.execute("insert into score (nombre,value) values (?,?)", (self.txt1._text, self.txt2._text))
                conexion.commit()# Actualiza los datos realmente en la tabla
            except:
                print("Error")
    
    def guardar_datos_ranking(self):
        
        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                # NO SE GUARDA LOS DATOS, CREATE TABLE 
                sentencia = ''' create  table score 
                                (
                                        id integer primary key autoincrement,
                                        nombre text,
                                        value real
                                )
                            '''
                conexion.execute(sentencia)
                print("Se creo la tabla personajes")                       
            except sqlite3.OperationalError:
                print("La tabla ya existe")

    def leer_datos_ranking(self):
        with sqlite3.connect("db/db_score.db") as conexion:
            cursor=conexion.execute("SELECT * FROM score")
            for fila in cursor:
                print(fila)

        
    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()