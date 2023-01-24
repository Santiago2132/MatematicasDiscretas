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
while True:
    #Ingreso de variables
    num1 = input("Ingresa el primer número hexadecimal: ")
    num2 = input("Ingresa el segundo número hexadecimal: ")
    #resultado 
    result = hex_sum(num1, num2)
    print (result)
    option = int(input("¿Quieres volver a sumar hexadecimales?  \n 1) Si \n 2) no \n Ingresa el número de la opción: "))
    if option == 2:
        break