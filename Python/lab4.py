import datetime
hora_actual = datetime.datetime.now()
#Atributos a usar
a = False
b = False
c = False
d = False
cont = 1
#Funciones
def booleano(a):
    if(a == 1):
        return True
    return False
def activar_alarma_s1():
    if a or c:
        print("\nAlarma S1 activada","\nLa hora emitida de la alarma:", hora_actual)
    else:
        print("\nS1 esta a salvo")
def activar_alarma_s2():
    if (c and(a or b or d)) or (a and b and d):
        print("\nAlarma S2 activada","\nLa hora emitida de la alarma:", hora_actual)
    else:
        print("\nS2 esta a salvo")
def activar_alarma_s3():
    if ((d and (c or b)) or (a)):
        print("\nAlarma S3 activada","\nLa hora emitida de la alarma:", hora_actual)
    else:
        print("\nS3 esta a salvo")
#Ingreso de datos
print("\nSistema de alarmas\n")
for i in range(4):
    try:
        while True:
            x = int(input("Ingrese el dato de la maquina: "))   
            if(x==0) or (x==1):
                break
            else:
                print("\nIngrese un valor entre 1 y 0\n")
    except ValueError:
        print("opción invalida")
    if(i == 0):
        a = booleano(x)
    if(i == 1):
        b = booleano(x)
    if(i == 2):
        c = booleano(x)
    if(i == 3):
        d = booleano(x)
activar_alarma_s1()
activar_alarma_s2()
activar_alarma_s3()