import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from constantes import *
import sqlite3

class Sql():

    @staticmethod #SQL.crear_datos_ranking 
    def crear_datos_ranking(nombre, score):
        with sqlite3.connect("ranking.db") as conexion:            
            try:
                conexion.execute("insert into score (nombre,value) values (?,?)", (nombre, score))
                conexion.commit()# Actualiza los datos realmente en la tabla
            except:
                print("Error")
    
    @staticmethod
    def guardar_datos_ranking():        
        with sqlite3.connect("ranking.db") as conexion:
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

    @staticmethod
    def leer_datos_ranking():
        lista_score = []
        with sqlite3.connect("ranking.db") as conexion:
            cursor=conexion.execute("SELECT * FROM score ORDER BY value ASC")
            nombre = [description[0] for description in cursor.description]
            for fila in cursor:
                score_dict = dict(zip(nombre, fila))
                lista_score.append(score_dict)
        return lista_score[:3]

    #################################################################################################
    '''
    def actualizar_tabla(nombre, score):
        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                conexion.execute("insert into scoreboard (nombre,score) values (?,?)", (nombre, score))
                conexion.commit()# Actualiza los datos realmente en la tabla
            except:
                print("Error")
    
    def crear_tabla():
        
        with sqlite3.connect("db/db_score.db") as conexion:
            try:
                sentencia =  # create  table scoreboard
                               # (
                                        #id integer primary key autoincrement,
                                       # nombre text,
                                        #score real
                               # )
                            
                conexion.execute(sentencia)
                print("Se creo la tabla highscore")                       
            except sqlite3.OperationalError:
                print("La tabla ya existe")

    def devolver_puntaje():
        lista_scoreboard = []
        with sqlite3.connect("db/db_score.db") as conexion:
            cursor=conexion.execute("SELECT nombre, score FROM scoreboard ORDER BY score DESC LIMIT 5")
            
            for fila in cursor:
                lista_scoreboard.append(fila)
        #print(lista_scoreboard)
        return lista_scoreboard
    
    '''
    