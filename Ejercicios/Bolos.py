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
print("Maquina de bolos")
#Listas del puntaje
tiros = [None]*100

#Tiros hasta nueve
rango = 0
for i in range(18):
    print("Turno ",i+1)
    if rango == 0:
        while True:
            x = int(int("Ingrese el primer tiro: "))
            if x >=0 or x <=10:
                tiros[i] = x
                break
    if rango == 1:
        while True:
            x = int(int("Ingrese el segundo tiro: "))
            if x >=0 or x <=10:
                tiros[i] = x
                break





#Primer tiro