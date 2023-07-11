import pygame
from constantes import *
from auxiliar import Auxiliar
from modo import * 

class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,interval_time_jump=100) -> None:        
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\stay({0}).png",0,5,flip=False,scale=3)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\stay({0}).png",0,5,flip=True,scale=3)        
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\walk({0}).png",0,3,flip=False,scale=3)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\walk({0}).png",0,3,flip=True,scale=3)
        self.run_r = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\run({0}).png",0,4,flip=False,scale=3)
        self.run_l = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\run({0}).png",0,4,flip=True,scale=3)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\jump({0}).png",0,4,flip=False,scale=3)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\jump({0}).png",0,4,flip=True,scale=3)
        self.jump_attack_r = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\jump.attack({0}).png",0,3,flip=False,scale=3,repeat_frame=3)
        self.jump_attack_l = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\jump.attack({0}).png",0,3,flip=True,scale=3,repeat_frame=3)
        self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\attack({0}).png",0,3,flip=False,scale=3)
        self.attack_l = Auxiliar.getSurfaceFromSeparateFiles("images\\caracters\\players\\Leonardo\\attack({0}).png",0,3,flip=True,scale=3)
        self.damaged_r = Auxiliar.getSurfaceFromSeparateFiles("images\caracters\players\Leonardo\damaged({0}).png",0,4,flip=False,scale=3)
        self.damaged_l = Auxiliar.getSurfaceFromSeparateFiles("images\caracters\players\Leonardo\damaged({0}).png",0,4,flip=True,scale=3)
        self.win_r = Auxiliar.getSurfaceFromSeparateFiles("images\caracters\players\Leonardo\win({0}).png",0,3,flip=False,scale=3)
        self.win_l = Auxiliar.getSurfaceFromSeparateFiles("images\caracters\players\Leonardo\win({0}).png",0,3,flip=True,scale=3)

        self.frame = 0
        self.lives = 6
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.pos_inicial_x = x
        self.pos_inicial_y = y
        self.rect.x = x
        self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/10,y,self.rect.width/2,self.rect.height)
        self.collition_rect_izq = self.rect.left
        self.collition_rect_der = self.rect.right
        self.collition_rect_bottom = self.rect.bottom
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H
        
        #Banderas 
        self.is_jump = False
        self.is_fall = False
        self.is_attack = False
        self.is_damage = False
        self.is_dead = False

        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 # en base al tiempo transcurrido general
        self.interval_time_jump = interval_time_jump
        self.cooldown_attack = 1000
        self.cooldown_damage = 0
        self.rect_disparos = pygame.Rect(self.collition_rect.x, self.rect.width,self.collition_rect.y, self.rect.height)
        self.rect_disparos.width = 1000
        self.rect_disparos.center = self.rect.center

        self.attack_sound = pygame.mixer.Sound("images\music\\attack.wav")
        self.damaged_sound = pygame.mixer.Sound("images\music\\damaged_soundeffect.wav")

    # ACCIONES 
    def walk(self,direction):
        if(self.is_jump == False and self.is_fall == False and self.is_damage == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def run(self):
        if (0 <= self.frame < len(self.animation)):
            if(self.direction == DIRECTION_R and self.is_jump == False and self.is_damage == False):
                self.move_x = self.speed_run
                self.animation = self.run_r                
            elif(self.direction == DIRECTION_L and self.is_jump == False and self.is_damage == False):
                self.move_x = -self.speed_run
                self.animation = self.run_l   
                
    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False and self.is_damage == False):
            self.y_start_jump = self.rect.y
            if (0 <= self.frame < len(self.animation)):
                if(self.direction == DIRECTION_R):
                    self.move_x = int(self.move_x / 2)
                    self.move_y = -self.jump_power
                    self.animation = self.jump_r
                else:
                    self.move_x = int(self.move_x / 2)
                    self.move_y = -self.jump_power
                    self.animation = self.jump_l
                self.frame = 0
                self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def attack(self):
        if (0 <= self.frame < len(self.animation)):        
            if(self.direction == DIRECTION_R):
                self.animation = self.attack_r
            else:
                self.animation = self.attack_l
            self.is_attack = True   
        self.attack_sound.play()         
        self.frame = 0

    def stay(self):
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l and self.is_jump == False and self.is_fall == False):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            elif(self.direction == DIRECTION_L):                
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def damaged(self):
            if self.is_damage:
                if (0 <= self.frame < len(self.animation)):
                    if self.direction == DIRECTION_R:
                        self.animation = self.damaged_r
                    else:
                        self.animation = self.damaged_l 
                    self.is_damage = False

    def receive_shoot(self):
        self.lives -= 1
        self.damaged_sound.play() 
        
    
    def death(self):
        if self.lives == 0:
            self.is_dead = True
    
    def win(self):
        if self.score == 900:
            if (0 <= self.frame < len(self.animation)):
                if self.direction == DIRECTION_R:
                    self.animation = self.win_r
                else:
                    self.animation = self.win_l
                self.frame += 1
                if self.frame >= len(self.animation):
                    self.frame = 0

    # Esenciales
    def change_x(self,delta_x):
        if (0<= self.rect.x + delta_x <= ANCHO_VENTANA - self.rect.width/2):        
            self.rect.x += delta_x
            self.collition_rect.x += delta_x
            self.ground_collition_rect.x += delta_x
            self.rect_disparos.x += delta_x


    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y     
        self.rect_disparos.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False     

            if self.animation == self.attack_r or self.animation == self.attack_l:
                self.is_attack = False       

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
            else: 
                self.frame = 0 
                if self.animation == self.attack_r or self.animation == self.attack_l:
                    self.is_attack = False
                    self.frame = 0         
 
    def update(self,delta_ms,plataform_list, enemy_list, boss):        
        for enemy in enemy_list:
            if self.collition_rect.colliderect(enemy.collition_rect):
                if self.cooldown_damage <= 0:
                    self.lives -= 1                    
                    self.is_damage = True
                    self.cooldown_damage = 3000  
            elif (self.collition_rect.colliderect(boss.collition_rect) and self.direction != boss.direction): 
                if self.cooldown_damage <= 0:
                    self.lives -= 1  
                    self.is_damage = True
                    self.cooldown_damage = 3000   

        if self.cooldown_damage > 0:
            self.cooldown_damage -= delta_ms

        if self.is_damage:
            self.damaged()
            self.damaged_sound.play()    

        
        
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
          

    '''
    ***En caso de aplicar dificultades***
                     o
                ***Boss*** 
    '''
    # def update(self,delta_ms,plataform_list, enemy_list):        
    #     for enemy in enemy_list:
    #         if self.collition_rect.colliderect(enemy.collition_rect):                
    #             self.lives -= 1
    #             self.rect.x = self.pos_inicial_x
    #             self.rect.y = self.pos_inicial_y
    #             self.collition_rect.x = self.pos_inicial_x
    #             self.collition_rect.y = self.pos_inicial_y
    #             self.ground_collition_rect.x = self.pos_inicial_x 
    #             self.ground_collition_rect.y = self.pos_inicial_y + self.rect.height - GROUND_COLLIDE_H 
    #     self.do_movement(delta_ms,plataform_list)
    #     self.do_animation(delta_ms)


    def draw(self,screen):
        
        if get_mode():
            pygame.draw.rect(screen,C_ORANGE,rect=self.collition_rect)
            pygame.draw.rect(screen,C_GREEN,rect=self.ground_collition_rect)
            pygame.draw.rect(screen,C_PINK,rect=self.rect_disparos)
        
        self.image = self.animation[self.frame]
        texto_puntaje = FUENTE_ESTADISTICAS.render("Puntaje: " + str(self.score), True, GREEN_TURTLE)
        screen.blit(texto_puntaje, (1400,10))
        screen.blit(self.image,self.rect)

    # Eventos
    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms

        if (keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_LSHIFT] and not keys[pygame.K_SPACE]):
            self.walk(DIRECTION_L)

        if (not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]and not keys[pygame.K_LSHIFT] and not keys[pygame.K_SPACE]):
            self.walk(DIRECTION_R)

        if (keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]):
            self.run()

        if (keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]):
            self.run()

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_LSHIFT]and not keys[pygame.K_x]):
            self.stay()

        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE] and not keys[pygame.K_LSHIFT]and not keys[pygame.K_x]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido
        
        if (keys[pygame.K_z]and not keys[pygame.K_SPACE] and not keys[pygame.K_LSHIFT]):
            self.jump_attack()
        
        if(keys[pygame.K_x]):
            self.attack()  