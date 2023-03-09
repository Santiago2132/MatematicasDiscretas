#Funciones
def mcd(a, b):#Maximo común divisor
    #Cambia de posición si el 2 digito es el mayor
    if b>a:
        a,b=b,a   
    #Iteraciones hasta b ser 0    
    while b:
        a, b = b, a % b        
    return a

#Primer punto
x = 6
for i in range(6):
    
