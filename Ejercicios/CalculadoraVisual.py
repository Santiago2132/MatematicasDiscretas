import tkinter as tk
#Funciones
def on_button_click():
    entered_text = entradanum1.get()
    try:
        entered_number1 = int(entered_text)
        print(entered_number1)
    except ValueError:
        print("Por favor ingresa un número válido.")
    entered_text = entradanum2.get()
    try:
        entered_number2 = int(entered_text)
        print(entered_number2)
    except ValueError:
        print("Por favor ingresa un número válido.")
    print(entered_number1+entered_number1)    
"Creación de la ventana"
ventana = tk.Tk()
#Tamaño de la ventana
ventana.geometry("400x300")
#Metodo para no hacer posible redimensionar el tamaño de la ventana
ventana.resizable(False, False)
#Titulo en la parte superior de la ventana
ventana.title("Calculadora Hexadecimal")
#Texto de etiqueta
"Etiquetas"
version = tk.Label(ventana,text = "Version.01")
#Dependiendo de lo que ponga despues la etiqueta sera puesta en una posición exacta
version.pack(side =tk.BOTTOM) #Opciones predeterminadas  BOTTOM/abajo Right/ Derecha  left/izquierda top/arriba

bienvenido  = tk.Label(ventana, text = "Bienvenido a la calculadora Hexadecimal")
bienvenido.pack(side = tk.TOP)
#Entrada de números
entradanum1 = tk.Entry() #Para el número 1
entradanum1.pack()#Aca podremos poner las caracteristicas de lo que estemos realizando
entradanum2 = tk.Entry() #Para el número 2
entradanum2.pack()#Aca podremos poner las caracteristicas de lo que estemos realizando
"Botones"
button = tk.Button(text="Sumar", command=on_button_click)
button.pack()


ventana.mainloop()
