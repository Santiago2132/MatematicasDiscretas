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
        semillas_ingresadas.append(X1)
        resultado[i] = numeros
        X2 = int(numeros)

        
    return resultado, semillas_ingresadas
semillas_ingresadas = []
#Programa principal
while True:#Falta culminar la salida de los números aleatorios.
    try:
        seed = int(input("Ingrese una semilla de 5 a 7 dígitos: "))               
        if len(str(seed)) < 5 or len(str(seed)) > 7:
            print("Error: la semilla debe tener entre 5 y 7 dígitos")
            continue
        elif len(set(str(seed))) == 1:
            print("Error: la semilla no puede tener todos los dígitos iguales")
            continue
        elif any(str(seed)[i:i+3] in '0123456789' for i in range(len(str(seed))-2)):
            print("Error: la semilla no puede tener números consecutivos")
            continue
        elif any(str(seed)[i:i+3] in '9876543210' for i in range(len(str(seed))-2)):
            print("Error: la semilla no puede tener números consecutivos")
            continue
        elif tredigitosiguales(seed):
            print("Error: la semilla no puede tener tres dígitos iguales")
            continue
        elif seed in semillas_ingresadas:
            print("Error: la semilla ya ha sido ingresada anteriormente")
            continue
        else:
            semillas_ingresadas.append(seed)
            numeros_aleatorios,semillas = algoritmoMultiplicadorConstante(seed, 36)            
            print("Números seudo aleatorios: ")
            for i in range(len(numeros_aleatorios)):
                print("0."+numeros_aleatorios[i])
            print("Semilla usada: ",seed)        
            print("Semillas usasdas: ",semillas) 
    except ValueError:
        print("Error: el valor ingresado no es un número")
        continue    
#Impresión de resutlados

