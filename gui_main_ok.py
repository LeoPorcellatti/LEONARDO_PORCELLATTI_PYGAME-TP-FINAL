import pygame
from pygame.locals import *
import sys
from constantes import * 
from gui_form import Form
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB
from gui_form_menu_C import FormMenuC
from gui_form_menu_game_l1 import FormGameLevel1
from gui_form_menu_principal import FormMenuPrincipal
from modo import * 
 
flags = DOUBLEBUF 
pygame.display.set_caption("TMNT")
icono = pygame.image.load("images\\gui\\menu\\icono.png")
pygame.display.set_icon(icono)
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA), flags, 16)
pygame.init()
clock = pygame.time.Clock()
# Pausa 
is_paused  = False
pausa = pygame.image.load("images\gui\menu\pause.png")
pausa = pygame.transform.scale(pausa,(500,500))

# Game OVer
game_over = False 


#form_menu_A = FormMenuA(name="form_menu_A",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(255,255,0),color_border=(255,0,255),active=True)
form_menu_principal = FormMenuPrincipal (name="form_menu_principal",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(255,255,0),color_border=(255,0,255),active=True)
form_menu_B = FormMenuB(name="form_menu_B",master_surface = screen,x=300,y=200,w=500,h=400,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_menu_C = FormMenuC(name="form_menu_C",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)
form_game_L1 = FormGameLevel1(name="form_game_L1",master_surface = screen,x=0,y=0,w=ANCHO_VENTANA,h=ALTO_VENTANA,color_background=(0,255,255),color_border=(255,0,255),active=False)

while True:     
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
        
        elif event.type == pygame.KEYDOWN:
            # Debug
            if event.key == pygame.K_TAB:
                cambiar_modo()
            # Pausa
            elif event.key == pygame.K_ESCAPE:
                is_paused = not is_paused
            

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    screen.fill("Light Green")

    if not is_paused:
        aux_form_active = Form.get_active()
        if(aux_form_active != None):
            aux_form_active.update(lista_eventos, keys, delta_ms)
            aux_form_active.draw()        
    else:
        screen.blit(pausa, (ANCHO_VENTANA / 2 - 250, ALTO_VENTANA / 2 - 250))

    pygame.display.flip()

 


    


  



