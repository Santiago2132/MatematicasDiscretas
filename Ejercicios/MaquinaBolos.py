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

tiro1 = [None] * 10 #Lista
tiro2 = [None] * 11 #Lista
resultados = [None] * 12
#Ingreso de datos
i=0
turno = 0
turn = 1
contador = 1
while i < 20:
    
    print("Turno ",contador)
    if turno == 0:
        while True:
                try:
                    tiro1[i] = int(input("Ingrese el primer tiro: "))                    
                    if tiro1[i] <= 10 or tiro1[i]  >= 0:
                        break
                    break
                except ValueError:
                    print("\n¡¡¡Ingrese un número!!!\n")
    if turno == 1:
        while True:
                tope = 10-tiro1[i-1]
                try:
                    tiro2[i-1] = int(input("Ingrese el primer tiro: "))                    
                    if tiro2[i-1] <= tope and tiro2[i-1] >= 0:
                        break
                    break
                except ValueError:
                    print("\n¡¡¡Ingrese un número!!!\n")
    if turn == 1:
        turn ==2
    if turn == 2:
        turn ==1
        contador = contador + 1
    if turno >0:
        turno = 0
    if turno < 0:
        turno = 1
print(tiro1)
print(tiro2)


#lanzamiento 10


#Puntaje
resultado = np.empty((10, 2))

