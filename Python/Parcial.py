def multiplicador_constante(seed, a, m, n):
    # seed: semilla inicial
    # a: constante multiplicativa
    # m: módulo
    # n: número de valores a generar
    
    # Inicializar la secuencia con la semilla
    xn = seed
    
    # Generar n valores de la secuencia
    for i in range(n):
        # Calcular el siguiente valor de la secuencia
        xn = (a*xn) % m
        
        # Normalizar el valor entre 0 y 1
        un = xn / m
        
        # Imprimir el valor generado
        print(un)

def generate_numbers(seed):
    results = []
    seeds = []
    while len(results) < 36:
        seed_product = seed*(seed+1)
        middle_digits = str(seed_product)[len(str(seed_product))//2:len(str(seed_product))//2+len(str(seed))]
        seed = int(middle_digits)
        if seed in seeds:
            print("Error: La semilla generada ya ha sido utilizada antes")
            return [], []
        results.append(seed)
        seeds.append(seed)
    return results, seeds

# Pedir al usuario la semilla
while True:
    try:
        seed = int(input("Ingrese una semilla de 5 a 7 dígitos: "))
        if len(str(seed)) < 5 or len(str(seed)) > 7:
            print("Error: la semilla debe tener entre 5 y 7 dígitos")
            continue
        elif len(set(str(seed))) == 1:
            print("Error: la semilla no puede tener todos los dígitos iguales")
            continue
        elif len(str(seed)) > len(set(str(seed))):
            print("Error: la semilla no puede tener dígitos repetidos")
            continue
        generate_numbers(seed)
    except ValueError:
        print("Error: el valor ingresado no es un número")
        continue
    else:
        break

# Generar los números seudo aleatorios
results, seeds = generate_numbers(seed)

# Imprimir los resultados
print(f"Semilla: {seed}")
print(f"Resultados: {results}")
print(f"Semillas utilizadas: {seeds}")