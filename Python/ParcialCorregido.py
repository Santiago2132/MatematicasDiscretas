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
#Funcion del producto medio 
'''
def multiplicador_constante(semilla, cantidad):
    tam1  = len(str(semilla))
    lista_semilla = [] #Lista para las semillas
    lista_numeros = [] #Lista de números aleatorios a generar
    lista_semilla.append(semilla)    
    a = 1103515245#parametros para generar los números seudo aleatorios
    c = 12345
    m = 2 ** 31    
    numero = semilla
    nueva_cantidad = cantidad // 2 # Nueva cantidad de números a generar
    for i in range(nueva_cantidad):
        numero = (a * numero + c) % m
        nx = numero / m        
        lista_numeros.append(numero / m)  
        lista_semilla.append(numero)
    return lista_numeros, lista_semilla
    '''
def producto_medio(semilla, cantidad):
    tam1  = len(str(semilla))
    lista_semilla = [] #Lista para las semillas
    lista_numeros = [] #Lista de números aleatorios a generar
    lista_semilla.append(semilla)
    numero1 = semilla
    #nueva_cantidad = cantidad // 2 # Nueva cantidad de números a generar
    for i in range(cantidad-1):
        numero2 = numero1 * lista_semilla[-1] #Se realiza la operación del producto de las semillas
        snumero2 = str(numero2) #Transforma el número generado en una string
        tam2 = len(snumero2) #Calcula el tamaño del número generado
        primerc = (tam2 - tam1) // 2 #Determina a partir de cual número se extrae la cadena de tam1 del calculo generado
        snumero3 = snumero2[primerc:primerc + tam1] #Se extrae la cadena de tam1 del cálculo generado
        lista_numeros.append(int(snumero3)) #Agrega la mitad del número generado a la lista de números
        lista_semilla.append(int(snumero3)) #Agrega la semilla generada a la lista de semillas
        numero1 = int(snumero3) #Actualiza la semilla para la siguiente iteración
    return lista_numeros, lista_semilla
#Programa principal
while True:#Falta culminar la salida de los números aleatorios.
    try:
        seed = int(input("Ingrese una semilla de 5 a 7 dígitos: "))        
        n = sum(int(d) for d in str(seed))
        if len(str(seed)) < 5 or len(str(seed)) > 7:
            print("Error: la semilla debe tener entre 5 y 7 dígitos")
            continue
        elif len(set(str(seed))) == 1:
            print("Error: la semilla no puede tener todos los dígitos iguales")
            continue
        elif any(str(seed)[i:i+3] in '0123456789' for i in range(len(str(seed))-2)):
            print("Error: la semilla no puede tener números consecutivos")
            continue
        elif tredigitosiguales(seed):
            print("Error: la semilla no puede tener tres dígitos iguales")
            continue
        else:
            numeros_aleatorios, semillas = producto_medio(seed, 36)            
            print(numeros_aleatorios)  
            print(semillas)
    except ValueError:
        print("Error: el valor ingresado no es un número")
        continue    
#Impresión de resutlados

