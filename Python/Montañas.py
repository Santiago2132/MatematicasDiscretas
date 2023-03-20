import math
print("      /\ \n     /_ \ \n    / \/ \ \n   /      \ \n  /        \ \n /          \ \n/            \Montañas")
#Funciones:
def tiempo (d,v): # Calcula el tiempo en el cual 
    tiempo = d/v
    return tiempo
def formulaDistancia(x1,y1,x2,y2): #Función para la distancia entre puntos: 
    x = (x2-x1)**2
    y = (y2-y1)**2
    distancia = math.sqrt(x - y)
    return distancia        

#Atributos si se requiere de entrada
vw = int(input("Ingrese la velocidad de caminata: "))
vc = int(input("Ingrese la velocidad cuando se excava el tunel: "))
cantCord = int(input("Cantidad de coordenadas:  "))#Ingreso de coordenadas
lista1 = []
lista2 = []
for i in range(cantCord):#Ingreso de puntos
    x = int(input("Ingrese la coordenada en x: "))
    y = int(input("Ingrese la coordenada en y: "))
    lista1.append(x)
    lista2.append(y)



i=0
tiempo = 0
penultimo = len(lista1)-1
while True:
    if i != penultimo:            
        if lista2[i] == lista2[i+2]:
            d1 = formulaDistancia(lista1[i],lista2[i],lista1[i+1],lista2[i+1])
            d2 = formulaDistancia(lista1[i],lista2[i],lista1[i+2],lista2[i+2])
            t1 = tiempo(d1,vw)
            t2 = tiempo(d2,vc)
            if (t2 > t1):
                tiempo = tiempo + t1
                i+=1
            else:
                tiempo = tiempo + t2
                i+=2
        else:
            d = formulaDistancia(lista1[i],lista2[i],lista1[i+1],lista2[i+1])
            caltiemp = d / vw               
            i+=1
    else:
        d = formulaDistancia(lista1[i],lista2[i],lista1[i+1],lista2[i+1])
        caltiemp = d / vw
        tiempo = tiempo + caltiemp
        break

print(tiempo)