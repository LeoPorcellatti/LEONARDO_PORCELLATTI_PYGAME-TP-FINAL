import pygame, sqlite3
import pygame.mixer
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
#from gui_form_menu_score import FormMenuScore
from gui_label import Label
from gui_textbox import *
from gui_progressbar import ProgressBar
from background import Background
from banderas import *
from gui_form_menu_B import FormMenuB


class FormMenuPrincipal(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)
        self.flag_sql = True        
        #self.boton1 = Button(master=self,x=760,y=200,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="",text="SUMA +",font="Verdana",font_size=30,font_color=C_WHITE)
        #self.boton2 = Button(master=self,x=910,y=200,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton2,on_click_param="",text="RESTA -",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton3 = Button(master=self,x=830,y=250,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\menu\\buttons\extras.png",on_click=self.on_click_boton1,on_click_param="form_menu_A",text="Volumen",font="Year supply of fairy cakes",font_size=25,font_color="Dark Red")
        self.boton6 = Button(master=self,x=830,y=320,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\menu\\buttons\Levels.png",on_click=self.on_click_boton2,on_click_param="form_contenedor_niveles",text="Niveles",font="Year supply of fairy cakes",font_size=25,font_color="Dark Red")
        self.boton7 = Button(master=self,x=830,y=390,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\menu\\buttons\SQL.png",on_click=self.on_click_boton3,on_click_param="form_menu_B",text="Ranking",font="Year supply of fairy cakes",font_size=25,font_color="Black")
        # self.boton3 = Button(master=self,x=760,y=320,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_game_L1",text="Nivel 1",font="Verdana",font_size=30,font_color=C_WHITE)
        # self.boton4 = Button(master=self,x=910,y=320,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_game_L2",text="Nivel 2",font="Verdana",font_size=30,font_color=C_WHITE)
        # self.boton5 = Button(master=self,x=830,y=380,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_game_L3",text="Nivel 3",font="Verdana",font_size=30,font_color=C_WHITE)
        
        # self.boton7 = Button(master=self,x=1360,y=550,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_contenedor_niveles",text="Niveles",font="Verdana",font_size=30,font_color=C_WHITE)
        # Original 
        # self.boton7 = Button(master=self,x=1360,y=550,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton3,on_click_param="form_menu_C",text="Vector",font="Verdana",font_size=30,font_color=C_WHITE)                        
        self.txt1 = TextBox(master=self,x=780,y=120,w=240,h=70,color_background=None,color_border=None,image_background="images\\gui\\menu\\textbox.png",text="",font="Year supply of fairy cakes",font_size=30,font_color="Light Green")
        # self.volumen = Label(master=self,x=780,y=260,w=240,h=50,color_background=None,color_border=None,image_background="images\gui\menu\label.png", text = "Label", font = "Arial", font_size=14, font_color=C_BLUE)
        #self.pb1 = ProgressBar(master=self,x=780,y=260,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 3, value_max=8)
        
        
        # if bandera_level_1 or bandera_level_2 or bandera_level_3:
        #     self.boton6 = Button(master=self,x=830,y=320,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\menu\\buttons\Levels.png",on_click=self.on_click_boton3,on_click_param="form_contenedor_niveles",text="Niveles",font="Year supply of fairy cakes",font_size=25,font_color="Dark Red")
        self.lista_widget = [self.boton3,self.boton6,self.boton7, self.txt1]
        

        # Archivo banderas        
                

        # Fondo 
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images\gui\menu\menu.png")
        self.dic_score = []
        
        # Música 
        pygame.mixer.music.load("images/music/00-Menu.wav")
        pygame.mixer.music.play()

    
    def on_click_boton1(self, parametro):
        self.set_active(parametro)
    
    def on_click_boton2(self, parametro):
        nombre = self.txt1.get_text()
        if len(nombre) > 0:
            self.set_active(parametro)
            banderas_niveles = {"nivel_1": False, "nivel_2": False, "nivel_3": False}
            crear_banderas(banderas_niveles)

        if self.flag_sql == True:
            with sqlite3.connect("ranking.db") as conexion:
                try:
                    sentencia = 'CREATE TABLE Ranking (nombre text, score integer)'
                    conexion.execute(sentencia)
                    # ELIMINAR
                    print("Ranking creado")

                except Exception as e:
                    # ELIMINAR  
                    print(f"Error en Base de datos {e}")
            self.flag_sql = False

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)
        for aux_widget in self.lista_widget:    
            aux_widget.draw()

    def on_click_boton3(self, parametro):
        self.set_active(parametro)
        nombre = self.txt1.get_text()
        ultimo_score = []
        
        with open("Datos_ranking.json", "r") as archivo:
            for linea in archivo:
                ultimo_score.append(linea)

        with sqlite3.connect("ranking.db") as conexion:
            print("Conexión a la base de datos establecida")
            try:
                print("entre",nombre,ultimo_score[0])
                sentencia = ' insert into Ranking (nombre, score) values(?,?)'
                conexion.execute(sentencia, (nombre, ultimo_score[0]))
                conexion.commit()
                print("Sentencia ejecutada correctamente")  # Agrega esta línea para verificar la ejecución
            except Exception as e:
                print(f"Error en Base de datos {e}")


        

        with sqlite3.connect("ranking.db") as conexion:
            try:
              
                sentencia = '''
                            select * from Ranking order by score desc limit 4
                            '''
                cursor = conexion.execute(sentencia)
                for fila in cursor:
                    print("select")
                    self.dic_score.append({"jugador" : f"{fila[0]}","Score":f"{fila[1]}"},)
                print("Tabla creada")
                #print(dic_score)
            except Exception as e:
                print(f"Error en Base de datos {e}")

    def get_score(self):
        return self.dic_score

    

    
        