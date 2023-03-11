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


    return resultado

numeros, semillas = producto_medio(1234567, 36)
print(numeros)
