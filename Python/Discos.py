import math
vt = 12
v0 = 1
vt, v0 = map(float, input().split()) #Pide los datos
i = 0
if math.pow(2,16)>v0 and math.pow(2,64) > vt: 
    while True:
        i += 1    
        y = i*i
        a = (vt/y)- v0
        if a >=0 :
            print("Hace el calculo del diamextro")        
            diametro = 0.3 * math.sqrt (vt/y - v0)
            print("Filas: ",i)
            print ("Diametro: ",diametro) 
            discos = diametro * y
            if discos > (math.pow(10,3)): 
                discos = discos % pow(10,3)
            if discos < (math.pow(10,3)):
                print ("Discos: ", discos)
        else:        
            break
