def mcd(a, b):
    #Cambia de posición si el 2 digito es el mayor
    if b>a:
        a,b=b,a   
    #Iteraciones hasta b ser 0    
    while b:
        a, b = b, a % b        
    return a
while True:
    #Impresión del bienvenido
    print("\nBienvenido al Maximo común divisor\n∵*.•´¸.•*´✶´ \n\n° ☆ ° ˛*˛☆_Π______˚☆\n*˚ ˛★˛•*/________/ ~ ⧹。˚ ˚\n˚ ˛•˛•˚  ｜ 田田 ｜門｜ ˚\n╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    #Ingreso de datos
    while True:#Primer número
        try:
            num1 = int(input("\nIngresa el primer número: "))
            break
        except ValueError:
            print("\nEl número ingresado no es un número")
    while True:#Segundo número
            try:
                num2 = int(input("\nIngresa el segundo número: "))
                break
            except ValueError:
                print("\nEl número ingresado no es un número")
    #resultado 
    print("Maximo común dividor: ",mcd(num1,num2))
    #Pregunta si se quiere realizar de nuevo el mcm
    while True:
        try:
            option = int(input("\n¿Quieres volver a calcular un MCD?  \n 1) Si \n 2) no \n Ingresa el número de la opción: "))
            break
        except ValueError:
            print("\nEl número ingresado no es un número")    
    if option == 2:
        print("\n Adios  :D...")
        break
