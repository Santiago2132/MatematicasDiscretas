import numpy as np
print("╔═════════════════════════════════╗\n║Bienvenido a cifrado y descifrado║\n╚═════════════════════════════════╝")
print("\n\n░░▄▀▀▀▄░▄▄░░░░░░╠▓░░░░\n░░░▄▀▀▄█▄░▀▄░░░▓╬▓▓▓░░\n░░▀░░░░█░▀▄░░░▓▓╬▓▓▓▓░\n░░░░░░▐▌░░░░▀▀███████▀\n▒▒▄██████▄▒▒▒▒▒▒▒▒▒▒▒▒ \n ")

while True:#Bucle principal del programa
    from math import gcd
    ALPHABET = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" #En efecto el alfabetoe
    #Funciones de entrada de datos
    

    def entdatos(n):
        while True:    
            key_input = input("\nLa matriz clave debe ser ingresada de la siguiente forma \n             ╔═══════════╗\nMatriz 2x2 = ║\"1 2, 3 4 \"║\n             ╚═══════════╝\n\n             ╔══════════════════════╗\nMatriz 3x3 = ║\"1 2 3, 3 4 6, 7 8 9 \"║\n             ╚══════════════════════╝\n DEBEN SER MATRICES CUADRADAS\n\nIntroduce la matriz clave (separada por comas y espacios): ")
            key_matrix = [[int(num) for num in row.split()] for row in key_input.split(",")]
            if len(key_matrix) not in [2, 3]:
                print("La matriz debe tener 2 o 3 filas")
                continue
            if any(len(row) != len(key_matrix) for row in key_matrix):
                print(" \nPor favor, ingresa una matriz cuadrada (nxn)\n")
                continue
            else: 
                break     
        if(n == 1):
            plaintext_input = input("Introduce el mensaje a cifrar: ")
            plaintext_input = plaintext_input.replace(" ","")
            try:
                print("\nEste es su mensaje cifrado: ",encrypt(plaintext_input.upper(), key_matrix))
            except ValueError:
                print("Error")        
        if(n == 2):
            ciphertext_input = input("Introduce el mensaje cifrado: ")
            ciphertext_input=  ciphertext_input.replace(" ","")
            try:        
                print("\nEste es su mensaje descifrado: ",decrypt(ciphertext_input.upper(), key_matrix))
            except ValueError:
                print("Error")
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
    #Desencriptación

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
    print("\n 1). Cifrar un texto \n 2). Descrifrar un texto \n 3). Apagar el programa")
    
    while True: #Elecciíon de opciones
        try:
            option = int(input("\nIngrese un número de una opción: "))
            break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.")            
    if(option == 1 or option == 2):
        entdatos(option)
    if  option == 3:
        print("\n ╔═════════════╗\n ║ Hasta luego ║\n ╚═════════════╝ \n")
        print("\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣙⣆⠀⠈⢳⡄⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠶⠟⠛⠉⠁⠉⠛⠃⠀⠈⣿⠻⠷⠶⣦⣤⣀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠀⠀⠀⠀⠀⠈⠙⢿⣦⣄⣀⣤ ⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠋⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀ ⠈⢿⣿⡉⢹⣿⣿⣿⣷⣶⣶⣤⠀⠀⠀⠀⠀⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀ ⠀⠀⠀⠀⠀⠀⠘⣿⣧⠀⢩⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⢀⠀⠘⣿⣷⡀⢉⣿⣿⣿⣿⡏\n⠀⠀⠀⠀⠀⠀⣠⣾⠃⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⠀ ⠀⠁⠀⠀⣿⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠘⣇⠀⠘⢿⣷⡉⠉⣿⣿⣿⠁\n⠀⠀⣀⣠⣴⣾⡿⠁⠀⠀⠀⠀⣿⠀⠀ ⠀⠀⠀⠀⠀⢰⡇⠀⠀⠸⣇⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⢻⡀⠀⠈⠻⣿⣮⡉⢹⡏⠀⠀⠀⠀ \n⢰⣿⣿⣿⣿⣿⠁⠀⢀⠀ ⠁⠀⢻⡆⠀⠀⠀⠀⠀⠀⢸⣧⠀⠀⠀⢻⡄⠀⠀⠀⢿⡀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠘⡿⣿⣿⣷⡀⠀\n⠘⣿⣿⣿  ⠇⠀⠀⣾⠀⠀⠀⢸⣧⠀⠀⠀⠀⠀⠀⠈⣿⣦⠀⠀⠈⢿⣄⠀⠀⠈⢷⡀⠀⠀⠀⠀⣷⠀⠀⠀⠀⢷⡀⠙⢿⣷⡀⠀⠀⠀⠀\n⠀⢻⣿⣿⡏⠀⢠⡀⢻⠀⠀⠀⢸⣿⣦⡀⠀⠀⠀⠀⠀⢿⡉⢷⡄⠀⠘⢿⣦⡀⠀⠈⢷⡀⠀⠀⠀⢻⠀⠀⠀⠀⠈⣧⠀⠈⢻⣷⡀⠀\n⠀⠘⣿⡿⠀⠀⣸⠀⣸⡇⠀⠀⢸⡇⠈⢷⣄⡀⠀⠀⠀⢺⣇⠀⠙⢦⣄⠈⢷⡹⢦⡀⠈⣷⠀⠀⠀⢸⡇⠀⠀⠀⠀⠸⣇ ⠀⠀⠹⣷⡀⠀\n⠀⠀⣸⡇⠀⠀⡯⢠⣿⢿⡄⠀⢸⡇⠀⠀⠈⠛⠶⣦⣄⣀⣹⣿⡓⠳⠎⠛⠲⠿⢦⣽⣶⣼⣇⠀⠀⢸⡇⠀ ⠀⠀⠀⠀⢻⡄⠀⠀⢻⣧\n⠀⢠⣿⠀⠀⠀⡇⣼⠏⠀⠻⣆⢘⣧⣴⠖⠋⠀⠀⠀⠀⠉⠁⠉⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿ ⡁⠀⢸⡇⠀⠀⠀⠀⠀⠘⣷⠀⠀⠈⣿⣇⠀\n⠀⣼⡟⠀⠀⠀⣿⡟⠀⠀⠀⠙⠳⠥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀ ⣀⣠⣤⣤⣼⡇⠀⢸⡇⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⡟⢿⣆⠀⠀\n⢀⣿⡇⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢀⣠⡤⢶⣾⣿⣿⣏⡹⠿⣇⠀⢸⡇⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⣧⠸⣿⡀⠀\n⢸⣿⢣⠀⠀⠀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⣶⣯⠵⠶⠛⠉⠁⠀⠀⠀⠀⢿⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀⣿⠀⣿⣧⠀⠀ \n⣸⡏⢹⠀⠀⠀⢿⡇⠀⠀⠀⣠⣤⣶⣾ ⣿⣻⣿⡿⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⠀⣀⠀⢸⡀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆ ⠀⡿⢰⡏⣿⡀\n⣿⡇⢸⡄⠀⠀⢸⣿⢀⣴⣟⣡⡽⠟⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⠸⣗⠻⠗⠻⠇⢸⡇⣸⠁⠀⠀⠀⠀ ⠀⠀⠀⢸⡇⠀⡇⢸⠇⢸⣧⠀ \n⣿⡅⠘⣇⠀⠀⠀⣿⡘⠛⠉⠁⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⢈⡇⣿ ⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢠⣃⡿⠀⠀⣿⠀ \n⣿⢷⡀⢹⡄⠀⠀⢹⡇⠀⠀⣸⡆⠶⠄⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡶⠃⠀⠀⠀ ⠀⠀⢸⣧⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠘⣼⠃⠀⠀⢻⡄\n⣿⠈⣧⠈⢷⠀⠀⠈⣿⠀⠀⠈⠀⠀⠀⠀⢀⠀⠀⢀⣀⣤⠴⠖⢚⣩⠽⠋ ⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⣰⠏⠀⠀⠀⢼⡇ \n⣿⠀⠘⣇⠘⣧⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠉⠛⠛⠷⠖⠒⠒ ⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⢁⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⢰⠟⠀⠀⠀⠀⣿⡄ \n⣿⡄⠀⠘⣦⠘⣇⠀⠈⣿⡄⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⠾⠋⢀⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⢨⡷⠋⠀⠀⠀⠀⠀⣿⠀ \n⢸⣧⠀⠀⠘⢧⡘⢧⡀⠘⠻⠶⢤ ⣤⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣴⣾⠟⠋⢀⣠⠶⢻⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠀⣰⡏⠀ \n⢿⡆⠀⠀⡈⢳⣄ ⠱⣄⠀⠀⠀⠀⠀⣽⠉⠉⢉⣉⠙⢿⣉⠉⠻⣿⡿⠋⢀⣠⠖⠋⠁⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⣠⡟⠀⠀\n⠈⢿ ⠀⠀⠀⠻⣾⣿⣛⣦⣄⠀⠈⠛⠲⠦⣄⣿⡇⠈⠙⠛⠶⠶⢶⣿⠀⠀⠀⢀⣴⣿⣿⣿⣯⣀⣀⣤⣤⣶⣿⣿⣿⣿ ⡛⠛⠋⠉⠉⠀⠀\n⠀⠀⠀⠀⠀⠘⣻⣷⣄⣙⡛⠶⠦⣤⣤⣄⣸⣷⡄⠀⠀⠀⢠⠏⣻⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⠛⣿⣿⣿⣿⣷⡀⠀⠀")
        print("")
        break
