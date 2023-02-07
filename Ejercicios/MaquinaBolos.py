import numpy as np
#funciones
def strike (tiro1,tiro2):
    if tiro1 ==10 or tiro2 ==10:
        return True
    return False
def tiro(turno):
    if turno >0:
        return 0
    if turno < 0:
        return 1
#Datos

#lanzamiento 10

#Puntaje

resultado = np.empty((10, 2))

