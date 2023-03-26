'''def metodo_productos_medios():    
    #Genera una secuencia de números pseudoaleatorios utilizando el algoritmo de productos medios.    
    semilla = int(input("Ingresa la primera semilla: "))
    semilla2 = int(input("Ingresa la segunda semilla: "))
    iterador = int(input("Ingrese la cantidad de iteraciones que deasea: "))    
    nums = []
    for n in range(iterador):
        
        product = semilla * semilla2    
        num = int(str(product)[len(str(product))//4:len(str(product))-len(str(product))//4])
        nums.append(num)
        print("("+str(n+1)+") "+" ("+str(semilla) + ")" + " * " + "("+str(semilla2) + ")" + " = ""0." + str(num))
        semilla = semilla2
        semilla2 = num  
            
    return nums

# Ejemplo de uso
print(metodo_productos_medios())'''

def validar_semilla(semilla):
    str_semilla = str(semilla)
    count = 1
    last_digit = str_semilla[0]
    for i in range(1, len(str_semilla)):
        if str_semilla[i] == last_digit:
            count += 1
            if count > 3:
                return False
        else:
            count = 1
            if str_semilla[i] == chr(ord(last_digit) + 1) or str_semilla[i] == chr(ord(last_digit) - 1):
                return False
        last_digit = str_semilla[i]
    return True

n = int(input("Ingrese el numero aleatorio a generar: "))
semilla = int(input("Ingrese una semilla de 5 a 7 digitos que no tenga digitos repetidos más de dos veces o sean consecutivos: "))

while len(str(semilla)) < 5 or len(str(semilla)) > 7 or not validar_semilla(semilla):
    semilla = int(input("Valor incorrecto, ingrese nuevamente una semilla de 5 a 7 digitos que no tenga digitos repetidos más de dos veces o sean consecutivos: "))

size = len(str(semilla))
xi = semilla

for i in range(n):
    xi = xi * xi
    str_xi = str(xi)
    ls = size // 2
    li = size + ls
    c = ""
    for j in range(len(str_xi) - li, len(str_xi) - ls):
        c += str_xi[j]
    xi = int(c)
    ri = float("0." + c)
    print(f"Este es xi [{i}]: {xi}       Esta es ri: {ri}")
    print()