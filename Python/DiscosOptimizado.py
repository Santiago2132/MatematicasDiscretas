import math
while True:
    while True:
        while True:
            try:
                vt = float(input("\nIngreso de masa total para discos: "))
                break
            except ValueError:
                print("¡Ingrese algo valido!")
                continue
        while True:
            try:
                v0 = float(input("Masa perdida en la forja de discos: "))
                break
            except ValueError:
                print("¡Ingrese algo valido!")
                continue
        if vt <= v0:
            print("Ingrese cantidades validas")
            continue
        else: 
            break
    i = 0
    if math.pow(2,16)>v0 and math.pow(2,64) > vt: 
        while True:
            i += 1
            y = i*i
            a = (vt/y)- v0
            if a >=0 :
                print("\nDatos y calculos")        
                diametro = 0.3 * math.sqrt (vt/y - v0)
                print("Filas: ",i)
                print ("Diametro: ",diametro) 
                discos = diametro * y
                if discos > (math.pow(10,3)): 
                    discos = discos % pow(10,3)
                    print ("Discos: ", discos)
                if discos < (math.pow(10,3)):
                    print ("Discos: ", discos)
            else:        
                break
