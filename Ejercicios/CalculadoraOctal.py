#Funciones 
#Octal a decimal
def octal_to_decimal(octal):
    decimal = 0
    octal = str(octal)
    for i in range(len(octal)):
        decimal += int(octal[i]) * (8 ** (len(octal) - i - 1))
    return decimal
#de decimal a  octal
def decimal_to_octal(decimal):
    octal = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        octal = str(remainder) + octal
    return octal
#Operaciones
#Suma
def oct_sum(a, b):
    decimal_a = octal_to_decimal(a)
    decimal_b = octal_to_decimal(b)
    decimal_sum = decimal_a + decimal_b
    octal_sum = decimal_to_octal(decimal_sum)
    return octal_sum
#Resta
def oct_rest(a, b):
    decimal_a = octal_to_decimal(a)
    decimal_b = octal_to_decimal(b)
    decimal_rest = decimal_a - decimal_b
    octal_rest = decimal_to_octal(decimal_rest)
    return octal_rest
#Multriplicación
def oct_mult(a, b):
    decimal_a = octal_to_decimal(a)
    decimal_b = octal_to_decimal(b)
    decimal_mult = decimal_a + decimal_b
    octal_mult = decimal_to_octal(decimal_mult)
    return octal_mult
#Division
def oct_div(a, b):
    decimal_a = octal_to_decimal(a)
    decimal_b = octal_to_decimal(b)
    decimal_div = decimal_a // decimal_b
    octal_div = decimal_to_octal(decimal_div)
    return octal_div

while True:
    #Impresión del bienvenido
    print("\nBienvenido a la calculadora Octal \n∵*.•´¸.•*´✶´ \n\n° ☆ ° ˛*˛☆_Π______˚☆\n*˚ ˛★˛•*/________/ ~ ⧹。˚ ˚\n˚ ˛•˛•˚  ｜ 田田 ｜門｜ ˚\n╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
    #Ingreso de datos

    num1 = input("\nIngresa el primer número Octal: ")
    
    num2 = input("\nIngresa el segundo número Octal: ")
    #resultado 
    result = oct_sum(num1, num2)
    print (result)
    option = int(input("¿Quieres volver a sumar hexadecimales?  \n 1) Si \n 2) no \n Ingresa el número de la opción: "))
    if option == 2:
        print("\n Adios  :D...")
        break