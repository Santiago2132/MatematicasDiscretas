#Función para saber si tiene 3 números iguales
def validar_semilla(semilla):
    str_semilla = str(semilla)
    count = 1
    last_digit = str_semilla[0]
    for i in range(1, len(str_semilla)):
        if str_semilla[i] == last_digit:
            count += 1
            if count > 2:
                return False
        else:
            count = 1
            if str_semilla[i] == str(int(last_digit) + 1) or str_semilla[i] == str(int(last_digit) - 1):
                return False
        last_digit = str_semilla[i]
    return True
#Funcion del producto medio 
def multiplicador_constante(semilla, cantidad):
    lista_semilla = [] #Lista para las semillas
    lista_numeros = [] #Lista de números aleatorios a generar
    lista_semilla.append(semilla)
    a = 1103515245
    c = 12345
    m = 2 ** 31    
    numero = semilla
    for i in range(cantidad):
        numero = (a * numero + c) % m
        lista_numeros.append(numero / m)  
        lista_semilla.append(numero)
    return lista_numeros, lista_semilla
#Programa principal
while True:
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
        elif validar_semilla(seed):
            print("Error: la semilla no puede tener tres dígitos iguales")
            continue
        else:
            numeros_aleatorios, semillas = multiplicador_constante(seed, 36)
            for i in range(36):
                print(numeros_aleatorios[i])
                print(semillas[i])  
    except ValueError:
        print("Error: el valor ingresado no es un número")
        continue
    else:
        break
#Impresión de resutlados

