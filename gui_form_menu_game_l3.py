import pygame
from auxiliar import *
from pygame.locals import *
from constantes import *
from gui_form import *
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from bullet import Bullet
from botin import Botin
from cronometro import Cronometro
from boss import Boss
from banderas import * 

class FormGameLevel3(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)        

        # --- GUI WIDGET ---                
        self.boton1 = Button(master=self,x=0,y=0,w=88,h=50,color_background=None,color_border=None,image_background="images\gui\menu\home.png",on_click=self.on_click_boton1,on_click_param="form_menu_principal",text="",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=100,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images\gui\menu\\buttons\Levels.png",on_click=self.on_click_boton1,on_click_param="form_contenedor_niveles",text="Niveles",font="Year supply of fairy cakes",font_size=25,font_color="Dark Red")
               
        self.pb_lives = ProgressBar(master=self,x=400,y=10,w=240,h=50,color_background=None,color_border=None,image_progress="images\\gui\\vidas\leonardo.png",value = 5, value_max=10)
        self.boss_lives = ProgressBar(master=self,x=1100,y=10,w=240,h=50,color_background=None,color_border=None,image_progress="images\\gui\\vidas\slash.png",value = 7, value_max=7)
        self.widget_list = [self.boton1,self.pb_lives, self.boss_lives, self.boton2]

        # --- GAME ELEMNTS --- 

        # Fondo
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images\locations\guarida.png")
        self.game_over_background = Background(x=0,y=0,width=w,height=h,path="images\gui\menu\game_over.png")
        self.win_background = Background(x=0,y=0,width=w,height=h,path="images\gui\menu\win.png")

        # Jugador
        self.player_1 = Player(x=0,y=400,speed_walk=8,speed_run=16,gravity=8,jump_power=16,frame_rate_ms=120,move_rate_ms=40,jump_height=150, interval_time_jump=300)
        self.boss_1 = Boss(x=1700, y=400, speed_walk=8, speed_run=16, gravity=8, jump_power=None, frame_rate_ms=120, move_rate_ms=40, jump_height=None, lives=5, interval_time_jump=None )

        # Enemigos
        self.enemy_list = []
        self.enemy_list.append (Enemy(x=1400,y=50,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,interval_time_jump=300, lives=1, enemy_type = 1))
        self.enemy_list.append (Enemy(x=500,y=50,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,interval_time_jump=300, lives=1, enemy_type = 1))
        self.enemy_list.append (Enemy(x=400,y=420,speed_walk=8,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,interval_time_jump=300, lives=1, enemy_type = 1))
        self.enemy_list.append (Enemy(x=1400,y=420,speed_walk=8,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,interval_time_jump=300, lives=1, enemy_type = 1))

        # Plataformas
        self.plataform_list = []
        self.plataform_list.append(Plataform(x=50, y=430, width=100, height=50,path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #izq
        self.plataform_list.append(Plataform(x=200, y=360, width=150, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #izq
        self.plataform_list.append(Plataform(x=50, y=250, width=100, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #izq
        self.plataform_list.append(Plataform(x=200, y=180, width=500, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #izq
        self.plataform_list.append(Plataform(x=700, y=400, width=400, height=50, path="images\platforms\plataforma_space.png", speed=5, frame_rate_ms = 150, move_rate_ms=50, type=1)) # medio
        self.plataform_list.append(Plataform(x=1650, y=430, width=100, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #Der
        self.plataform_list.append(Plataform(x=1650, y=250, width=100, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #Der
        self.plataform_list.append(Plataform(x=1500, y=360, width=150, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #Der
        self.plataform_list.append(Plataform(x=1000, y=180, width=500, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #Der

        # Bullet
        self.bullet_list = []
        

        # Botin
        self.botin_list = []
        self.botin_list.append(Botin(x=1650, y=200, width=75, height=75, path = "images\\Botin\\botin(2).png", type = 3))
        self.botin_list.append(Botin(x=200, y=300, width=75, height=75, path = "images\\Botin\\botin(2).png", type = 3))
        self.botin_list.append(Botin(x=900, y=505, width=75, height=75, path = "images\\Botin\\botin(2).png", type = 3))
        self.botin_list.append(Botin(x=1650, y=375, width=75, height=75, path = "images\\Botin\\botin(2).png", type = 3))

        # Cronometro
        self.cronometro = Cronometro(x=750, y=10, tiempo_limite=500)
        
        # Game Over
        self.game_over = False
        self.win = False
        self.cronometro = Cronometro(x=750, y=10, tiempo_limite=300000)

        # CD Shoot
        self.can_shoot = True
        self.shoot_cooldown = 3000
        self.last_shoot_time = 0   

        # Win
        self.cowabunga = pygame.mixer.Sound("images\music\\cowabunga.wav")
    
    def reset_level(self):
        # Jugador
        self.player_1 = Player(x=0,y=400,speed_walk=8,speed_run=16,gravity=8,jump_power=16,frame_rate_ms=120,move_rate_ms=40,jump_height=150, interval_time_jump=300)
        self.boss_1 = Boss(x=1700, y=400, speed_walk=8, speed_run=16, gravity=8, jump_power=None, frame_rate_ms=120, move_rate_ms=40, jump_height=None, lives=5, interval_time_jump=None )

        # Enemigos
        self.enemy_list = []
        self.enemy_list.append (Enemy(x=1400,y=50,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,interval_time_jump=300, lives=1, enemy_type = 1))
        self.enemy_list.append (Enemy(x=500,y=50,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,interval_time_jump=300, lives=1, enemy_type = 1))
        self.enemy_list.append (Enemy(x=400,y=420,speed_walk=8,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,interval_time_jump=300, lives=1, enemy_type = 1))
        self.enemy_list.append (Enemy(x=1400,y=420,speed_walk=8,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,interval_time_jump=300, lives=1, enemy_type = 1))

        # Plataformas
        self.plataform_list = []
        self.plataform_list.append(Plataform(x=50, y=430, width=100, height=50,path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #izq
        self.plataform_list.append(Plataform(x=200, y=360, width=150, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #izq
        self.plataform_list.append(Plataform(x=50, y=250, width=100, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #izq
        self.plataform_list.append(Plataform(x=200, y=180, width=500, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #izq
        self.plataform_list.append(Plataform(x=700, y=400, width=400, height=50, path="images\platforms\plataforma_space.png", speed=5, frame_rate_ms = 150, move_rate_ms=50, type=1)) # medio
        self.plataform_list.append(Plataform(x=1650, y=430, width=100, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #Der
        self.plataform_list.append(Plataform(x=1650, y=250, width=100, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #Der
        self.plataform_list.append(Plataform(x=1500, y=360, width=150, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #Der
        self.plataform_list.append(Plataform(x=1000, y=180, width=500, height=50, path="images\platforms\plataforma_space.png", speed=0, frame_rate_ms = 150, move_rate_ms=50, type=1)) #Der

        # Bullet
        self.bullet_list = []
        

        # Botin
        self.botin_list = []
        self.botin_list.append(Botin(x=1650, y=200, width=75, height=75, path = "images\\Botin\\botin(2).png", type = 3))
        self.botin_list.append(Botin(x=200, y=300, width=75, height=75, path = "images\\Botin\\botin(2).png", type = 3))
        self.botin_list.append(Botin(x=900, y=505, width=75, height=75, path = "images\\Botin\\botin(2).png", type = 3))
        self.botin_list.append(Botin(x=1650, y=375, width=75, height=75, path = "images\\Botin\\botin(2).png", type = 3))

        # Cronometro
        self.cronometro = Cronometro(x=750, y=10, tiempo_limite=500)
        
        # Game Over
        self.game_over = False
        self.win = False
        self.cronometro = Cronometro(x=750, y=10, tiempo_limite=300000)

        # CD Shoot
        self.can_shoot = True
        self.shoot_cooldown = 3000
        self.last_shoot_time = 0   

    def automatic_shoot(self):
        self.contador_cd = pygame.time.get_ticks() 

        for self.enemy in self.enemy_list:
            if self.enemy.collition_rect.colliderect(self.player_1.rect_disparos) and self.can_shoot and self.player_1.lives > 0 and self.enemy.lives >0:
                if self.enemy.direction == DIRECTION_R:
                    self.bullet_list.append(Bullet(self.enemy, self.enemy.rect.right, self.enemy.rect.centery, 1800, self.enemy.rect.centery, 5, path="images\\Enemigos\\robot_bullt(1).png", frame_rate_ms=100, move_rate_ms=20, width=80, height=10))
                    self.can_shoot = False
                    self.last_shoot_time = self.contador_cd
                elif self.enemy.direction == DIRECTION_L:
                    self.bullet_list.append(Bullet(self.enemy, self.enemy.rect.right, self.enemy.rect.centery, 0, self.enemy.rect.centery, 5, path="images\\Enemigos\\robot_bullt(1).png", frame_rate_ms=100, move_rate_ms=20, width=80, height=10))
                    self.can_shoot = False
                    self.last_shoot_time = self.contador_cd

            if not self.can_shoot and self.contador_cd - self.last_shoot_time >= self.shoot_cooldown:
                self.can_shoot = True
                

    def on_click_boton1(self, parametro):
        self.set_active(parametro)
        self.reset_level()

    def on_click_shoot(self, parametro):
        if self.player_1.lives > 0:
            for enemy_element in self.enemy_list:
                self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,20,path="images\\Enemigos\\robot_bullt(0).png",frame_rate_ms=100,move_rate_ms=20,width=80,height=10))
  
    def update(self, lista_eventos,keys,delta_ms):        

        if not self.game_over and not self.win:  
            for aux_widget in self.widget_list:
                aux_widget.update(lista_eventos)
                
            for bullet_element in self.bullet_list:
                bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)

            for plataforma in self.plataform_list:
                plataforma.update()

            for enemy_element in self.enemy_list:
                enemy_element.update(delta_ms,self.plataform_list, self.player_1)
                if enemy_element.lives == 0:
                    self.enemy_list.remove(enemy_element)            
                        
            self.player_1.events(delta_ms,keys)
            self.player_1.update(delta_ms,self.plataform_list, self.enemy_list, self.boss_1)     

            self.boss_1.update(delta_ms,self.plataform_list, self.player_1)         

            for botin in self.botin_list:
                botin.update(self.player_1)    

            self.pb_lives.value = self.player_1.lives 
            self.boss_lives.value = self.boss_1.lives 
            self.automatic_shoot()

        if self.game_over or self.win:
            for aux_widget in self.widget_list:
                aux_widget.update(lista_eventos)  

    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for botin in self.botin_list:
            botin.draw(self.surface)
        
        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)   
        
        self.player_1.draw(self.surface)

        self.boss_1.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)

        self.cronometro.draw(self.surface)
         
        if self.player_1.lives == 0 or self.cronometro.time_out:
            self.game_over = True
            self.game_over_background.draw(self.surface)
            self.boton2 .draw()  

        if self.boss_1.lives == 0:
            self.cowabunga.play()            
            self.win_background.draw(self.surface)
            self.boton2.draw() 
            modificar_banderas(True, "nivel_3")