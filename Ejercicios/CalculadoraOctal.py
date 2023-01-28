#Funciones 

def octal_to_decimal(octal):
    decimal = 0
    octal = str(octal)
    for i in range(len(octal)):
        decimal += int(octal[i]) * (8 ** (len(octal) - i - 1))
    return decimal

print(octal_to_decimal('12')) # Output: 10

#de decimal a  octal
def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        octal = str(remainder) + octal
    return octal

print(decimal_to_octal(10)) # Output: '12'
#Operaciones
#Suma
def oct_sum(a, b):
    decimal_a = int(a, 16)
    decimal_b = int(b, 16)
    decimal_sum = decimal_a + decimal_b
    oct_sum = octal_to_decimal(decimal_sum)
    return oct_sum

num1 = octal_to_decimal(23)
num2 = octal_to_decimal(22)
print("Prueba de suma: ",oct_sum(num1,num2))