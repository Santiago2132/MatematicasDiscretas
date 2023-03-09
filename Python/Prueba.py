def tredigitosiguales(num):
    digitos = []
    # Convertir el número en una cadena y recorrer cada dígito
    for digito in str(num):
        # Convertir el dígito en un entero y agregarlo a la lista
        digitos.append(int(digito))
    # Creación de la función
    for i in range(len(digitos)):
        cont = 0
        for j in range(len(digitos)):
            if digitos[i] == digitos[j]:
                cont += 1
            if cont >= 3:
                return True
    return False

print(tredigitosiguales(212121))