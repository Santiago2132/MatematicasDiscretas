#Funciones
#Aun no funciona
#Conversor de decimal a hexadecimal
def decimal_to_hex(decimal):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while decimal > 0:
        remainder = decimal % 16
        decimal = decimal // 16
        result = hex_digits[remainder] + result
    return result
#Division de Hexadecimales
def hex_div(a, b):
    decimal_a = int(a, 16)
    decimal_b = int(b, 16)
    decimal_sum = decimal_a - decimal_b
    hex_div = decimal_to_hex(decimal_sum)
    return hex_div
while True:
    #Ingreso de variables
    num1 = input("Ingresa el primer número hexadecimal: ")
    num2 = input("Ingresa el segundo número hexadecimal: ")
    #resultado 
    result = hex_div(num1, num2)
    print (result)
    option = int(input("¿Quieres dividir hexadecimales?  \n 1) Si \n 2) no \n Ingresa el número de la opción: "))
    if option ==1:
        hex_div(num1, num2)
    if option ==2:
        break
    else:
        break