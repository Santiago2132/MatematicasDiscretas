while True:
    semilla = input("Escriba semilla: ")
    tam1 = len(semilla) #Determina el tamaño de la semilla
    print("Cantidad de dígitos: ", tam1) #Dependiendo del tamaño de la semilla sera la longitud de los números generados
    numero1 = int(semilla)
    for i in range(10):
        numero2 = numero1**2 #Se realiza la operación del cuadrado de la semilla
        snumero2 = str(numero2) #Transforma el número generado en una string
        tam2 = len(snumero2) #Calcula el tamaño del número generado
        primerc = int((tam2 - tam1) / 2)
        snumero3 = snumero2[primerc:primerc+tam1]   
        x = "0."
        print ("{}. {}{}".format(i+1,x,snumero3))
        numero1 = int(snumero3)
    try:
        option = int(input("Ingresa '1' si quieres generar más digitos seudo aleatorios:  "))
        if option != 1:
            break;
    except ValueError:
        print("¡Ingrese un número!")