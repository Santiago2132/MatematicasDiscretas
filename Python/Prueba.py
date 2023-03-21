import numpy as np
while True:
    from math import gcd

    ALPHABET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    #Funciones de entrada de datos
    #Funciones de cifrado y descigrado
    def encrypt(plaintext, key):
        n = len(key)        
        # Check if key has an inverse modulo len(ALPHABET)
        det = int(round(np.linalg.det(key)))
        if gcd(det, len(ALPHABET)) != 1:
            raise ValueError("La matriz clave no tiene una inversa módulo {}".format(len(ALPHABET)))        
        # Create matrix from plaintext
        plaintext_matrix = []
        row = []
        for i in range(len(plaintext)):
            row.append(ALPHABET.index(plaintext[i]))
            if (i+1) % n == 0:
                plaintext_matrix.append(row)
                row = []        
        # Fill remaining spaces with 'X'
        if len(row) > 0:
            while len(row) < n:
                row.append(ALPHABET.index('X'))
            plaintext_matrix.append(row)        
        # Encrypt matrix
        encrypted_matrix = np.dot(key, np.transpose(plaintext_matrix)) % len(ALPHABET)        
        # Convert encrypted matrix to ciphertext
        ciphertext = ""
        for j in range(encrypted_matrix.shape[1]):
            for i in range(n):
                ciphertext += ALPHABET[encrypted_matrix[i][j]]        
        # Separate ciphertext into groups of 4 characters
        separated_ciphertext = ' '.join([ciphertext[i:i+4] for i in range(0, len(ciphertext), 4)])        
        return separated_ciphertext
    
    key_input = input("Introduce la matriz clave (separada por comas y espacios): ")
    key_matrix = [[int(num) for num in row.split()] for row in key_input.split(",")]
    plaintext_input = input("Introduce el mensaje a cifrar: ")
    plaintext_input = plaintext_input.replace(" ","")

    try:
        print(encrypt(plaintext_input.upper(), key_matrix))
    except ValueError as e:
        print(e)
    #Desencriptación
    ALPHABET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    def decrypt(ciphertext, key):
        n = len(key)
        det = int(round(np.linalg.det(key)))
        det_inv = pow(det, -1, len(ALPHABET))
        key_inv = (det_inv * np.round(det * np.linalg.inv(key)).astype(int) % len(ALPHABET)).astype(int)        
        plaintext = ""
        # Create matrix from ciphertext
        ciphertext_matrix = []
        row = []
        for i in range(len(ciphertext)):
            row.append(ALPHABET.index(ciphertext[i]))
            if (i+1) % n == 0:
                ciphertext_matrix.append(row)
                row = []        
        # Fill remaining spaces with 'X'
        if len(row) > 0:
            while len(row) < n:
                row.append(ALPHABET.index('X'))
            ciphertext_matrix.append(row)        
        # Decrypt matrix
        decrypted_matrix = np.dot(key_inv, np.transpose(ciphertext_matrix)) % len(ALPHABET)        
        # Convert decrypted matrix to plaintext
        for j in range(decrypted_matrix.shape[1]):
            for i in range(n):
                plaintext += ALPHABET[decrypted_matrix[i][j]]        
        return plaintext
    def cifradoHill(texto, clave):
        n = len(clave)
        textoNumeros = [ord(letra) - 65 for letra in texto]
        if len(textoNumeros) % n != 0:
            textoNumeros += [0] * (n - len(textoNumeros) % n)
        clave = np.array(clave)
        textoCifradoNumeros = []
        for i in range(0, len(textoNumeros), n):
            subTexto = textoNumeros[i:i+n]
            subTextoCifrado = np.dot(clave, subTexto) % 26
            textoCifradoNumeros.extend(subTextoCifrado)
        textoCifrado = ''.join([chr(num + 65) for num in textoCifradoNumeros])
        return textoCifrado
    
    key_input = input("Introduce la matriz clave (separada por comas y espacios): ")
    key_matrix = [[int(num) for num in row.split()] for row in key_input.split(",")]
    ciphertext_input = input("Introduce el mensaje cifrado: ")
    ciphertext_input=  ciphertext_input.replace(" ","")
    print(decrypt(ciphertext_input.upper(), key_matrix))
