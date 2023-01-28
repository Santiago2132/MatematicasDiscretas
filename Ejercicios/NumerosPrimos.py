#Como saber si los números son primos
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print("\nPrueba\n ")
i=0
while i<101:    
    x = prime(i)
    print("El número (",i,") es primo:",x)
    i = i + 1