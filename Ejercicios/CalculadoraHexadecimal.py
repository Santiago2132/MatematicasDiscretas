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
#Tiene errores en casos concretos falta terminar
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
    decimal_multiply = decimal_a * decimal_b
    hex_rest = decimal_to_hex(decimal_multiply)
    return hex_rest
#Division de hexadecimales
def hex_division(a, b):
    decimal_a = int(a, 16)
    decimal_b = int(b, 16)
    decimal_division = decimal_a / decimal_b
    hex_rest = decimal_to_hex(decimal_division)
    return hex_rest
#Entradas de hexadecimales
num1 = input("Ingresa el primer número hexadecimal: ")
num2 = input("Ingresa el segundo número hexadecimal: ")

#Opciones de la calculadora
opcion = 0
print("───────────────────────────────\n───────────────████─███────────\n──────────────██▒▒▒█▒▒▒█───────\n─────────────██▒────────█──────\n─────────██████──██─██──█──────\n────────██████───██─██──█──────\n────────██▒▒▒█──────────███────\n────────██▒▒▒▒▒▒───▒──██████───\n───────██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███─\n──────██▒▒▒▒─────▒▒▒▒▒▒▒▒▒▒▒▒█─\n──────██▒▒▒───────▒▒▒▒▒▒▒█▒█▒██\n───────██▒▒───────▒▒▒▒▒▒▒▒▒▒▒▒█\n────────██▒▒─────█▒▒▒▒▒▒▒▒▒▒▒▒█\n────────███▒▒───██▒▒▒▒▒▒▒▒▒▒▒▒█\n─────────███▒▒───█▒▒▒▒▒▒▒▒▒▒▒█─\n────────██▀█▒▒────█▒▒▒▒▒▒▒▒██──\n──────██▀██▒▒▒────█████████────\n────██▀███▒▒▒▒────█▒▒██────────\n█████████▒▒▒▒▒█───██──██───────\n█▒▒▒▒▒▒█▒▒▒▒▒█────████▒▒█──────\n█▒▒▒▒▒▒█▒▒▒▒▒▒█───███▒▒▒█──────\n█▒▒▒▒▒▒█▒▒▒▒▒█────█▒▒▒▒▒█──────\n██▒▒▒▒▒█▒▒▒▒▒▒█───█▒▒▒███──────\n─██▒▒▒▒███████───██████────────\n──██▒▒▒▒▒██─────██─────────────\n───██▒▒▒██─────██──────────────\n────█████─────███──────────────\n────█████▄───█████▄────────────\n──▄█▓▓▓▓▓█▄─█▓▓▓▓▓█▄───────────\n──█▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓█──────────\n──█▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓█──────────\n──▀████████▀▀███████▀──────────") 
while True: 
   
   print("""
   Bienvenido

   Dime, ¿qué quieres hacer?
   
   1) Sumar los dos números
   2) Restar los dos números
   3) Multiplicar los dos números
   4) Dividir los dos números
   5) Cambiar los números elegidos
   6) Apagar calculadora

   """) #Pregunta que es lo que quiere hacer
   while True:  
      try: 
         opcion = int(input("Elige una opción: ") )
         break
      except ValueError:
         print("Elige solo numeros del 1 al 6")

   #Opciones
   if opcion == 1:   #Sumar los dos numeros
      print(" ")
      print("RESULTADO: La suma de",num1,"+",num2,"es igual a",hex_sum(num1,num2))
   elif opcion == 2:    #Restar los dos numeros
      print(" ")
      print("RESULTADO: La resta de",num1,"-",num2,"es igual a",hex_rest(num1,num2))
   elif opcion == 3:    #Multiplica los dos numeros
      print(" ")
      print("RESULTADO: El producto de",num1,"*",num2,"es igual a",hex_multiply(num1,num2))
    
    #No funciona la division en hexadecimal

   #elif opcion == 4:    #Divide los dos numeros
    #    print("RESULTADO: El producto de",num1,"/",num2,"es igual a",hex_division(num1,num2))

   elif opcion == 5:       #Vuelve a preguntar los dos numeros
      
        num1 = input("Introduce tu primer número hexadecimal: ")
    
        num2 = input("Introduce tu segundo número: ")
                     

   elif opcion == 6:    #Cierra la calculadora
      break
   else:
      print("Opción incorrecta")
