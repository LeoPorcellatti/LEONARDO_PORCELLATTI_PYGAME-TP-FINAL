from gui_form_menu_game_l1 import FormGameLevel1
from gui_form_menu_game_l2 import FormGameLevel2
from gui_form_menu_game_l3 import FormGameLevel3 

class Reset_Level:
    def __init__(self, formularios_niveles):
        self.formularios_nivels = formularios_niveles

    def reiniciar_nivel(self):
        for formulario in self.formularios_nivels:
            if formulario.game_over or formulario.win:
                formulario.reset_level()
