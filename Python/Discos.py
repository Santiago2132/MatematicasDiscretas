import math
def disk(a,b):
    x = b * b
    z = a * x
    return z
vt = 16
v0 = 2
i = 0
while True:
    i += 1
    y = i*i
    a = (vt/y)- v0
    if a >=0 :
        print("Hace el calculo del diamextro")
        diametro = 0.3 * math.sqrt (vt/y - v0)
        print ("Diametro: ",diametro) 
        print ("Discos: ",disk(diametro,i))
    else:        
        break
