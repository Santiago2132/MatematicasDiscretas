#Funciones
#Conversor de decimal a hexadecimal
def decimal_to_hex(decimal):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while decimal > 0:
        remainder = decimal % 16
        decimal = decimal // 16
        result = hex_digits[remainder] + result
    return result
#Suma de Hexadecimales
def hex_sum(a, b):
    decimal_a = int(a, 16)
    decimal_b = int(b, 16)
    decimal_sum = decimal_a + decimal_b
    hex_sum = decimal_to_hex(decimal_sum)
    return hex_sum
#Resta de hexadecimales
def hex_rest(a, b):
    decimal_a = int(a, 16)
    decimal_b = int(b, 16)
    decimal_rest = decimal_a - decimal_b
    hex_rest = decimal_to_hex(decimal_rest)
    return hex_rest
#Multiplicacion de hexadecimales
def hex_multiply(a, b):
    decimal_a = int(a, 16)
    decimal_b = int(b, 16)
    decimal_rest = decimal_a * decimal_b
    hex_rest = decimal_to_hex(decimal_rest)
    return hex_rest
#Division de hexadecimales
def hex_division(a, b):
    decimal_a = int(a, 16)
    decimal_b = int(b, 16)
    decimal_rest = decimal_a * decimal_b
    hex_rest = decimal_to_hex(decimal_rest)
    return hex_rest
#Entradas de hexadecimales
num1 = input("Ingresa el primer número hexadecimal: ")
num2 = input("Ingresa el segundo número hexadecimal: ")
valid_options = ["option1", "option2", "option3"]

user_input = input("Please choose an option: ")
while user_input not in valid_options:
    print("Invalid option. Please choose a valid option.")
    user_input = input("Please choose an option: ")

print("You chose:", user_input)
result = hex_sum(num1, num2)
print("La suma en hexadecimal es:", result)
