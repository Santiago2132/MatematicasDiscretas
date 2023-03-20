#Programa algebra lineal
import numpy as np

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

key_input = input("Introduce la matriz clave (separada por comas y espacios): ")
key_matrix = [[int(num) for num in row.split()] for row in key_input.split(",")]
ciphertext_input = input("Introduce el mensaje cifrado: ")

print(decrypt(ciphertext_input.upper(), key_matrix))