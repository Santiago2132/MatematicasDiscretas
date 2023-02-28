def cuadrados_medios(semilla, digitos):
    # Calcula el número de dígitos necesarios para el cuadrado de la semilla
    d = len(str(semilla**2))
    # Genera números pseudoaleatorios a partir de la semilla
    for i in range(digitos):
        # Calcula el cuadrado de la semilla y lo convierte a una cadena de caracteres
        cuadrado = str(semilla**2)
        # Añade ceros a la izquierda si es necesario para obtener un número de dígitos igual a d
        while len(cuadrado) < 2*d:
            cuadrado = '0' + cuadrado
        # Extrae el número de dígitos deseados del centro del cuadrado y lo convierte a un número entero
        inicio = (len(cuadrado) - d) // 2
        fin = inicio + d
        semilla = int(cuadrado[inicio:fin])
        # Normaliza el número generado entre 0 y 1
        aleatorio = semilla / (10**d)
        # Devuelve el número generado
        yield aleatorio
a = float(input("\nIngreso de semilla: "))
b = float(input(" Cantidad de digitos: "))
print(cuadrados_medios(a,b))