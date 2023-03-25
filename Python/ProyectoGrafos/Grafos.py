#No funciona ¿
from tkinter import*
import tkinter as tk

ventana = tk.Tk()
ventana.title("Grafos")
ventana.geometry("400x300")
ventana.config(bg = "grey")
miFrame = Frame()
miFrame.pack()

miImagen = PhotoImage(file ="imagen.jpg")
mi_canvas = Canvas(ventana,width=800,height=700)
mi_canvas.config(fil = "both", expand = True)
mi_canvas.create_image(fil = "both", image = miImagen, anchor = "nw")
ventana.mainloop()