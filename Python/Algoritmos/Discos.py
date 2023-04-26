import math

while True:
    while True:
        try:
            vt = float(input("\nIngreso de masa total para discos: "))
            v0 = float(input("Masa perdida en la forja de discos: "))
            if vt <= v0:
                print("Ingrese cantidades validas")
                continue        
            else: 
                break
        except ValueError:
            print("¡Ingrese algo valido!")
    i = 0
    valorAnterior = 0
    if math.pow(2, 16) > v0 and math.pow(2, 64) > vt:
        print("Calculo de la longitud maxima")
        while True:
            i += 1    
            y = i*i
            a = (vt/y) - v0
            if a >= 0:    
                diametro = 0.3 * math.sqrt(vt/y - v0)
                discos = diametro * y
                if discos > math.pow(10, 3): 
                    discos = discos % math.pow(10, 3)
                if discos < valorAnterior:
                    print("Fila: ", i - 1,"\nMaximo número estirado: ", int(valorAnterior),"\nDiametro maximo: ", diametroAnterior)
                    break
                valorAnterior = discos
                diametroAnterior = diametro
            else:        
                break
        break
    if math.pow(2, 16) < v0 or math.pow(2, 64) < vt:
        print("\n Cantidades no validas ")
        continue
