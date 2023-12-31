from player import *
from constantes import *
from auxiliar import Auxiliar
from modo import * 

class Enemy():
    
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height, lives, enemy_type, interval_time_jump=100):
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images\\Enemigos\\robot_stay({0}).png",0,5,scale=3)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images\\Enemigos\\robot_stay({0}).png",0,5,flip=True,scale=3)
        self.shot_r = Auxiliar.getSurfaceFromSeparateFiles("images\\Enemigos\\robot_shot({0}).png",0,8,scale=3)
        self.shot_l = Auxiliar.getSurfaceFromSeparateFiles("images\\Enemigos\\robot_shot({0}).png",0,8,flip=True,scale=3)

        self.contador = 0
        self.frame = 0
        self.lives = lives
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.walk_r
        self.type = enemy_type
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/10,y,self.rect.width/2,self.rect.height)
        self.collition_rect_izq = self.rect.left
        self.collition_rect_der = self.rect.right
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        # self.cooldown_shot = 0 # pasar por parametro para diferentes tiempos de disparo
        # self.cooldown_shot_time = 3000 

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
        self.shoot_cooldown = 0
        #self.vision = pygame.Rect(0, 0, 150, 20)

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        # print(self.rect.y)   

    def disparo(self):
        pass

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                self.is_fall = False
                self.change_x(self.move_x)
                if self.contador <= 50:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
                    self.contador += 1 
                    self.direction = DIRECTION_L
                elif self.contador <= 100:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                    self.direction = DIRECTION_R
                    self.contador += 1
                else:
                    self.contador = 0
        
    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno          

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                #print(self.frame)
            else: 
                self.frame = 0
        

    def update(self,delta_ms,plataform_list, player):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        if player.is_attack: 
            if self.rect.colliderect(player.collition_rect):
                self.lives -= 1
                player.score += 300
              

    def draw(self,screen):
        
        if get_mode():
            pygame.draw.rect(screen,C_RED,rect=self.collition_rect)
            pygame.draw.rect(screen,C_GREEN,rect=self.ground_collition_rect)

        if self.lives > 0:
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

    def receive_shoot(self):
        self.lives -= 1
