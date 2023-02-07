import numpy as np
#funciones
def strike (tiro1,tiro2):
    if tiro1 ==10 or tiro2 ==10:
        return True
    return False
#Datos
matrix = np.empty((100, 100))#Matriz
tiro1 = [None] * 10 #Lista
tiro2 = [None] * 11 #Lista
resultados = [None] * 12
#Puntaje
for i in range(9):
    print("Turno ",i+1)
    for j in range(2):
        if j == 0: #Ingreso del primer tiro
            while True:
                try:
                    matrix[i][j] = int(input("Ingrese el primer tiro: ".format(i, j)))                    
                    if matrix[i][j]<= 10 or matrix[i][j] >= 0:
                        break
                    break
                except ValueError:
                    print("\n¡¡¡Ingrese un número!!!\n")
            print()
        if j == 1: #Ingreso del segundo tiro
            while True:
                try:
                    matrix[i][j]= int(input("Ingrese el segundo tiro: ".format(i, j)))
                    tope = 10 - matrix[i][0]                    
                    if matrix[i][j] <= tope and matrix[i][j] >= 0:
                        break                    
                except ValueError:
                    print("\n¡¡¡Ingrese un número!!!\n")
            print()
#lanzamiento 10
print (matrix)
#puntos
resultado = np.empty((10, 2))

for i in range(10):  
    if i == 0:
        resultado[i][0] = matrix[i][0] + matrix[i]
    #Strike