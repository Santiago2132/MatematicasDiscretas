def algoritmoMultiplicadorConstante(semilla, cantNumeros):
    resultado = [0] * cantNumeros  # Se inicializa la lista con la cantidad de números a generar
    X1 = int(semilla)  # Se convierte la semilla a un entero
    X2 = 9803  # X2 es igual a X1 en el primer lugar
    for i in range(cantNumeros):
        X2 = X1 * X2        
        longitud = len(str(X2))
        indice = (longitud // 2) - 2
        numeros = str(X2)[indice:indice+4]
        resultado[i] = numeros
    return resultado

list = algoritmoMultiplicadorConstante(6965,36)
print(list)