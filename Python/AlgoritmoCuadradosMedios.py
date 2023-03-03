while True:
    while True:
        semilla = input("Escriba semilla: ")
        if len(semilla) > 3:
            break
    tam1 = len(semilla) #Determina el tamaño de la semilla
    print("Cantidad de dígitos: ", tam1) #Dependiendo del tamaño de la semilla sera la longitud de los números generados
    numero1 = int(semilla) # Conversor de la semilla un entero
    for i in range(10):
        numero2 = numero1**2 #Se realiza la operación del cuadrado de la semilla
        snumero2 = str(numero2) #Transforma el número generado en una string
        tam2 = len(snumero2) #Calcula el tamaño del número generado
        primerc = int((tam2 - tam1) / 2)#Determina a partir de cual número se extrae la cadena de tam1 del calculo generado
        snumero3 = snumero2[primerc:primerc+tam1]#Se arma la cadena a partir del primer digito
        x = "0."
        print ("{}.  {}{}".format(i+1,x,snumero3))#Imprime de manera seccionada entre el número de i y el número generado
        numero1 = int(snumero3)
    try:
        option = int(input("Ingresa '1' si quieres generar más digitos seudo aleatorios:  "))
        if option != 1:
            break;
    except ValueError:
        print("¡Ingrese un número!")
