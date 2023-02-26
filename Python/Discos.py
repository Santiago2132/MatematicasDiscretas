import math
def diameter(a,b,c):
    if c == 1:
        return 0.3 * math.sqrt(a - b)
    if c > 1:
        return 0.3 * math.sqrt(a/c*c - b)
def positive(a):    
    if a > 0:
        return True
    if a < 0:
        return False
vt = 12
v0 = 1
v = vt 
i = 0
while True:
    print ("Entro")
    i += 1
    y = i*i
    a = (vt/y)- v0
    if positive(a) == True:
        print("Hace el calculo del diametro")
        diametro = 0.3 * math.sqrt (vt/y - v0)
        print ("Diametro: ",diametro)        
    if positive(a) == False:        
        break
diametro = round(diametro,4)
i -= 1
x = i * i
z = diametro * x
print (z)
