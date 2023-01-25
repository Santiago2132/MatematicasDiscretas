#Como saber si los números son primos
def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(prime(2)) # True
print(prime(3)) # True
print(prime(4)) # False