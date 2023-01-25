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
#Verificacion de números hexadecimales
def is_hex_number(string):
    if not string:
        return False
    hex_digits = set("0123456789abcdefABCDEF")
    for char in string:
        if char not in hex_digits:
            return False
    return True

#Suma de Hexadecimales
def hex_sum(a, b):
    decimal_a = int(a, 16)
    decimal_b = int(b, 16)
    decimal_sum = decimal_a + decimal_b
    hex_sum = decimal_to_hex(decimal_sum)
    return hex_sum

#Suma
while True:
    #Impresión del bienvenido
    print("\nBienvenido a la suma Hexadecimal \n∵*.•´¸.•*´✶´ \n\n° ☆ ° ˛*˛☆_Π______˚☆\n*˚ ˛★˛•*/________/ ~ ⧹。˚ ˚\n˚ ˛•˛•˚  ｜ 田田 ｜門｜ ˚\n╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    #Ingreso de datos

    num1 = input("\nIngresa el primer número hexadecimal: ")
    if is_hex_number(num1)==False:        
        while True:
            print("\nInvalid")          
            num1 = input("\nIngresa el primer número hexadecimal: ")
            if is_hex_number(num1)==True:
                break
    num2 = input("\nIngresa el segundo número hexadecimal: ")
    if is_hex_number(num2)==False:        
        while True:
            print("\nInvalid")         
            num2 = input("\nIngresa el segundo número hexadecimal: ")
            if is_hex_number(num2)==True:
                break                       
    #resultado 
    result = hex_sum(num1, num2)
    print (result)
    option = int(input("¿Quieres volver a sumar hexadecimales?  \n 1) Si \n 2) no \n Ingresa el número de la opción: "))
    if option == 2:
        print("\n Adios  :D...")
        break