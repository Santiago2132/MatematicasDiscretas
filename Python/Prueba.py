import tkinter
ventana = tkinter.Tk()
ventana.geometry("400x300")
def saludo():
    hola = tkinter.Tk()
    hola.geometry("200x100")
    hola.resizable(False, False)
    etiqueta = tkinter.Label(hola, text = "Hola",bg = "green")
    etiqueta.pack(fill = tkinter.BOTH, expand = True)
    #print("Hola")#Esto se genera por terminal
etiqueta = tkinter.Label(ventana, text = "Calculadora Hola mundo", bg = "gray")
text = tkinter.Entry(ventana)
text.pack()
def getext():
    text1 = text.get()
    print(text1)
    return text1

boton1 = tkinter.Button(ventana, text = "Presiona", padx = 40, pady = 10, command = saludo)# padx o y determina el tamaño del botón
boton1.pack()#Para ponerlo
#etiqueta.pack(fill = tkinter.BOTH, expand = True)# al nombrarlo asi abarcara todo X, o todo Y, pero con BOTH y true
#Abarca todo el espacio posible

#etiqueta.pack(side = tk.RIGHT)#Con esto se pone a la izquierda en la mitad de la 

#ventana.resizable(False, False)#Con esta linea hacemos que el programa no sea reescalables
ventana.mainloop()