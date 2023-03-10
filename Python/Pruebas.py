#Algoritmo de cuadrados medios flexible 
def algoritmo_cuadrados_medios(semilla, cant_numeros): # primera ingresa la semilla y luego la cantidad de número seudo aleatorios a generar
    resultado = []
    tam1 = len(semilla) #Determina el tamaño de la semilla
    numero1 = int(semilla) #Conversor de la semilla a un entero
    for i in range(cant_numeros):
        numero2 = numero1**2 #Se realiza la operación del cuadrado de la semilla
        snumero2 = str(numero2) #Transforma el número generado en una string
        tam2 = len(snumero2) #Calcula el tamaño del número generado
        primerc = int((tam2 - tam1) / 2)#Determina a partir de cual número se extrae la cadena de tam1 del calculo generado
        snumero3 = snumero2[primerc:primerc+tam1]#Se arma la cadena a partir del primer digito
        resultado.append(int(snumero3))
        numero1 = int(snumero3)
    return resultado
#Función para saber si tiene 3 números iguales
def tredigitosiguales(num): #Ya funciona
    digitos = []
    # Convertir el número en una cadena y recorrer cada dígito
    for digito in str(num):
        # Convertir el dígito en un entero y agregarlo a la lista
        digitos.append(int(digito))
    # Creación de la función
    for i in range(len(digitos)):
        cont = 0
        for j in range(len(digitos)):
            if digitos[i] == digitos[j]: #Se recorre la misma lista con el fin de comparar si existen iguales
                cont += 1#Con ello almacenando y si llega a 3, retornar verdadero
            if cont >= 3:
                return True
    return False
#Programa principal
while True:#Falta culminar la salida de los números aleatorios.
    try:
        seed = int(input("Ingrese una semilla de 5 a 7 dígitos: "))
        if len(str(seed)) < 5 or len(str(seed)) > 7:#Verifica la cantidad de digitos que tiene el número 
            print("Error: la semilla debe tener entre 5 y 7 dígitos")
            continue
        elif len(set(str(seed))) == 1: #Verifica que no tenga todos los digitos iguales
            print("Error: la semilla no puede tener todos los dígitos iguales")
            continue
        elif any(str(seed)[i:i+3] in '0123456789' for i in range(len(str(seed))-2)): # verifica la secuencia no sea igual
            print("Error: la semilla no puede tener números consecutivos")
            continue
        elif tredigitosiguales(seed): # Que no tenga 3 digitos repetidos
            print("Error: la semilla no puede tener tres dígitos iguales")
            continue
        else:
            seed = str(seed) #cambia de int a string, aunque se podría cambiar pero buenoooooo
            print(algoritmo_cuadrados_medios(seed, 36)) #El segundo numerito es para la cantidad de numeros a dar, solamente que no recuerdo el valor exacto entonces puse el mio          
    except ValueError:
        print("Error: el valor ingresado no es un número")
        continue
    else:
        break