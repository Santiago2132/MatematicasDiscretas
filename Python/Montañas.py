import math
print("      /\ \n     /_ \ \n    / \/ \ \n   /      \ \n  /        \ \n /          \ \n/            \Montañas")
#Funciones:
def calcularDistanciaEntrePuntos(x1, x2, y1, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def calcularDistanciaHorizontal(x1, x2):
    return abs(x2 - x1)

cantidad = int(input("Ingrese la cantidad de puntos: "))
coordenadasX = []
coordenadasY = []

for i in range(cantidad):
    x = float(input(f"Ingrese la coordenada X del punto {i+1}: "))
    y = float(input(f"Ingrese la coordenada Y del punto {i+1}: "))
    coordenadasX.append(x)
    coordenadasY.append(y)

vc = float(input("Ingrese la velocidad de cavar: "))
vw = float(input("Ingrese la velocidad de caminar: "))

distancia = 0
tiempoMin = 0

for i in range(cantidad):
    if i+1 != cantidad:
        distanciaMont = calcularDistanciaEntrePuntos(coordenadasX[i], coordenadasX[i+1], coordenadasY[i], coordenadasY[i+1])
        if ((coordenadasY[i] > 0 and coordenadasY[i+1] < 0) or (coordenadasY[i] < 0 and coordenadasY[i+1] > 0) or (coordenadasY[i] == coordenadasY[i+1])):
            distancia += distanciaMont
            tiempoMin += distanciaMont / vw
        else:
            distanciaHorizontal = calcularDistanciaHorizontal(coordenadasX[i], coordenadasX[i+1])
            if vw > vc or vw < vc:
                tiempoMont = distanciaMont / vw
                tiempoCueva = distanciaHorizontal / vc
                if tiempoMont > tiempoCueva:
                    tiempoMin += tiempoCueva
                else:
                    tiempoMin += tiempoMont
            if vw == vc:
                if distanciaMont > distanciaHorizontal:
                    tiempoMin += distanciaHorizontal / vc
                else:
                    tiempoMin += distanciaMont / vw
print("El tiempo es: ", tiempoMin)
