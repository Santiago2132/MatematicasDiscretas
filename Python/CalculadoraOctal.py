#Funciones 
#Comprobador de octal
def isoctal(num):
    for char in num:
        if char < '0' or char > '7':
            return False
    return True
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
#Comienzo del programa
#Impresión del bienvenido
print("\nBienvenido a la calculadora Octal \n∵*.•´¸.•*´✶´ \n\n° ☆ ° ˛*˛☆_Π______˚☆\n*˚ ˛★˛•*/________/ ~ ⧹。˚ ˚\n˚ ˛•˛•˚  ｜ 田田 ｜門｜ ˚\n╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬")
while True:
    #Ingreso de datos
    num1 = input("\nIngresa el primer número Octal: ")#Primer número
    if isoctal(num1) == False:#Comprobar si el número es octal
        while True:
            print("\n Invalid \n")
            num1 = input("\nIngresa el primer número Octal: ")
            if isoctal(num1)==True:
                break
    num2 = input("\nIngresa el primer número Octal: ")#Segundo número
    if isoctal(num2) == False:#Comprobar si el número es octal
        while True:
            print("\n Invalid \n")
            num2 = input("\nIngresa el primer número Octal: ")
            if isoctal(num2)==True:
                break
    print("""
    Opciones:
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos números
    5) Cambiar los números elegidos
    6) Apagar calculadora
    """) #Pregunta que es lo que quiere hacer
    while True:  #Ingreso de opción
        try: 
            opcion = int(input("Elige una opción: ") )
            break
        except ValueError:
            print("¡Elige solo numeros del 1 al 6!")
    #Opciones
    if opcion == 1:   #Sumar los dos numeros
        print(" ")
        print("RESULTADO: La suma de",num1,"+",num2,"es igual a",oct_sum(num1,num2))
    elif opcion == 2:    #Restar los dos numeros
        print(" ")
        print("RESULTADO: La resta de",num1,"-",num2,"es igual a",oct_rest(num1,num2))
    elif opcion == 3:    #Multiplica los dos numeros
        print(" ")
        print("RESULTADO: El producto de",num1,"*",num2,"es igual a",oct_mult(num1,num2))
    elif opcion == 4:    #Divide los dos numeros
        print("RESULTADO: El producto de",num1,"/",num2,"es igual a",oct_div(num1,num2))
    elif opcion == 5:       #Vuelve a preguntar los dos numeros      
        num1 = input("Introduce tu primer número hexadecimal: ")    
        num2 = input("Introduce tu segundo número: ")   
    elif opcion == 6:    #Cierra la calculadora
        break
    else:
        print("Opción incorrecta")