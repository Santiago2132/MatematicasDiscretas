import numpy as np
#Funciones
def isnumber(a): #Maxima cantidad de jugadores
    if a<0:
        return False
    if a >10:
        return False
    return True
def strike(a): #Cuando sea un strike
    if a == 10:
        return True
    else:
        return False
#Datos
while True:#Cantidad de jugadores
    try: 
        jugadores = int(input("Ingresa la cantidad de jugadores: "))
        if isnumber(jugadores)==False:
            print("\n¡¡¡Son maximo 10 jugadores!!!\n")
        if isnumber(jugadores)==True:            
            break
    except ValueError:
        print("Debe ingresar números")
matrix = np.empty((jugadores, 21))#Matriz
#Puntaje
for i in range(jugadores):
    for j in range(21): 
        puntaje = int(input("Ingrese el puntaje: ".format(i, j)))
        matrix[i][j] = puntaje
        if strike(puntaje) == True:
            j += 1


Score = np.empty((jugadores, 21)) #Puntaje final aun sin sistematizar
