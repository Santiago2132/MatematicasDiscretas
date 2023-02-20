#Maximo común divisor
def mcd(a, b):        
    while b:
        a, b = b, a % b       
    return a
#Minimo común multiplo
def mcm(a,b):
    return int(a*b/mcd(a,b))
while True:
    #Impresión del bienvenido
    print("\nBienvenido al minimo común multiplo\n∵*.•´¸.•*´✶´ \n\n° ☆ ° ˛*˛☆_Π______˚☆\n*˚ ˛★˛•*/________/ ~ ⧹。˚ ˚\n˚ ˛•˛•˚  ｜ 田田 ｜門｜ ˚\n╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    #Ingreso de datos
    while True:#Primer número
        try:
            num1 = int(input("\nIngresa el primer número: "))
            break
        except ValueError:
            print("\nEl número ingresado no es un número")
    while True: #Segundo número
            try:
                num2 = int(input("\nIngresa el segundo número: "))
                break
            except ValueError:
                print("\nEl número ingresado no es un número")
    #resultado 
    print("Minimo común multiplo: ",mcm(num1,num2))
    #Pregunta si se quiere realizar de nuevo el mcm
    while True:
        try:
            option = int(input("¿Quieres volver a calcular un mcm?  \n 1) Si \n 2) no \n Ingresa el número de la opción: "))
            break
        except ValueError:
            print("\nEl número ingresado no es un número")
    if option == 2:
        print("\n Adios  :D...")
        break