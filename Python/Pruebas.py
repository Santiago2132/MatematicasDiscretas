def entrada(n):
        while True:
            try:
                key_input = input("Introduce la matriz clave (separada por comas y espacios): ")
                key_matrix = [[int(num) for num in row.split()] for row in key_input.split(",")]                
            except ValueError:
                print("\nIngrese una clave valida!\n ")
            if ValueError == True:                
                continue
            if ValueError == False:
                break
        
        if(n == 1):
            plaintext_input = input("Introduce el mensaje a cifrar: ")
            plaintext_input = plaintext_input.replace(" ","")
            
x = int(input("Ingrese la opción"))
entrada(x)