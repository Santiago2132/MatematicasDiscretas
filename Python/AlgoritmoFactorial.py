def factorial_in_number(num):
    """
    Calcula la suma de los factoriales de los dígitos de un número
    """
    # Convertimos el número en una cadena de caracteres
    num_str = str(num)
    
    # Inicializamos la suma de los factoriales en 0
    factorial_sum = 0
    
    # Iteramos por cada dígito en el número
    for digit in num_str:
        # Convertimos el dígito en un entero
        digit_int = int(digit)
        
        # Calculamos el factorial del dígito
        factorial = 1
        for i in range(1, digit_int+1):
            factorial *= i
        
        # Sumamos el factorial al total
        factorial_sum += factorial
    
    # Devolvemos la suma de los factoriales
    return factorial_sum

#Algoritmo base
lista = []
n = int(input("Ingrese un número entero: "))
print(factorial_in_number(n))
'''
while True:
    n = int(input("Ingrese un número entero: "))
    while True:
        if(n>0):
            y = anterior_factorial(n)
            x = n  - y
            n = x
            lista.append(n)
            continue
        else:
            break
    print(lista)'''