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

def algoritmoMultiplicadorConstante(semilla, cantNumeros):
    num_digits = len(str(semilla))
    resultado = [0] * cantNumeros  # Se inicializa la lista con la cantidad de números a generar
    X1 = int(semilla)  # Se convierte la semilla a un entero
    X2 = X1  # X2 es igual a X1 en el primer lugar    
    semillas_ingresadas = []
    for i in range(cantNumeros):
        numeros = str(X1 * X2)
        longitud = len(numeros)
        indice = (longitud // 2) - 2                                                                                                   
        numeros = numeros[indice:indice+num_digits]
        semillas_ingresadas.append(X2)
        resultado[i] = numeros
        X2 = int(numeros)
        
    return resultado
semillas_ingresadas = []

def ordenamiento (numeros):

    modificar = True 
    
    while modificar: 
        modificar = False
        for i in range(len(numeros) - 1):
            if numeros [i] > numeros [i + 1]:
                #Se realiza el cambio
                numeros [i], numeros [i + 1] = numeros [i + 1], numeros [i]
                modificar = True
                #print(numeros [i], numeros [i + 1])
        return numeros

#Inicio del programa
semilla = int(input(" Ingresa la semilla: "))
cantidad = int(input(" Ingresa la cantidad de números a generar: "))

nums = algoritmoMultiplicadorConstante(semilla, cantidad)
numerosOrdenados = ordenamiento(nums)
print(nums)
print(numerosOrdenados)
