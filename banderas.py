import json

def crear_banderas(banderas_niveles):
    with open("Banderas_Niveles.json", "w") as archivo:
        json.dump(banderas_niveles, archivo)

def leer_banderas(path):
    with open("Banderas_Niveles.json", "r") as archivo:
        banderas_niveles = json.load(archivo)

def modificar_banderas(nuevo_valor, nivel):
    with open("Banderas_Niveles.json", "r") as archivo:
        banderas_niveles = json.load(archivo)

    banderas_niveles[nivel] = nuevo_valor

    with open("Banderas_Niveles.json", "w") as archivo:
        json.dump(banderas_niveles, archivo)
