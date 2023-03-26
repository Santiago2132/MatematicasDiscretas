#Funciones
#Conversor de decimal a hexadecimal
def decimaltohex(decimal):
    hex_digits = "0123456789ABCDEF"
    result = ""
    while decimal > 0:
        remainder = decimal % 16
        decimal = decimal // 16
        result = hex_digits[remainder] + result
    return result
#Verificacion de números hexadecimales
def ishexnumber(string):
    if not string:
        return False
    hex_digits = set("0123456789abcdefABCDEF")
    for char in string:
        if char not in hex_digits:
            return False
    return True

#Suma de Hexadecimales
def hexsum(a, b):
    decimal_a = int(a, 16)
    decimal_b = int(b, 16)
    decimal_sum = decimal_a + decimal_b
    hex_sum = decimaltohex(decimal_sum)
    return hex_sum

#Suma
while True:
    #Impresión del bienvenido
    print("\nBienvenido a la suma Hexadecimal \n∵*.•´¸.•*´✶´ \n\n° ☆ ° ˛*˛☆_Π______˚☆\n*˚ ˛★˛•*/________/ ~ ⧹。˚ ˚\n˚ ˛•˛•˚  ｜ 田田 ｜門｜ ˚\n╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    #Ingreso de datos

    num1 = input("\nIngresa el primer número hexadecimal: ")
    if ishexnumber(num1)==False:        
        while True:
            print("\nInvalid")          
            num1 = input("\nIngresa el primer número hexadecimal: ")
            if ishexnumber(num1)==True:
                break
    num2 = input("\nIngresa el segundo número hexadecimal: ")
    if ishexnumber(num2)==False:        
        while True:
            print("\nInvalid")         
            num2 = input("\nIngresa el segundo número hexadecimal: ")
            if ishexnumber(num2)==True:
                break                       
    #resultado 
    result = hexsum(num1, num2)
    print (result)
    option = int(input("¿Quieres volver a sumar hexadecimales?  \n 1) Si \n 2) no \n Ingresa el número de la opción: "))
    if option == 2:
        print("\n Adios  :D...")
        break