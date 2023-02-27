import math

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
    while True:
        i += 1    
        y = i*i
        a = (vt/y) - v0
        if a >= 0:
            print("Hace el calculo del diametro")        
            diametro = 0.3 * math.sqrt(vt/y - v0)
            print("Filas: ", i)
            print("Diametro: ", diametro) 
            discos = diametro * y
            print("Discos: ", discos)         
            if discos > math.pow(10, 3): 
                discos = discos % math.pow(10, 3)
            if discos < valorAnterior:
                print("Fila: ", i - 1)
                print("Maximo número estirado: ", int(valorAnterior))
                print("Diametro maximo: ", diametroAnterior)
                break
            valorAnterior = discos
            diametroAnterior = diametro
        else:        
            break
