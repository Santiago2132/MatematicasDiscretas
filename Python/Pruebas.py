import tkinter as tk

# Función para mostrar la ventana principal
def mostrar_ventana_principal():
    # Creamos la ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana principal")

    # Creamos un botón para abrir la otra ventana
    boton_otra_ventana = tk.Button(ventana_principal, text="Abrir otra ventana", command=mostrar_otra_ventana)
    boton_otra_ventana.pack()

    # Ejecutamos el bucle de la ventana principal
    ventana_principal.mainloop()

# Función para mostrar la otra ventana
def mostrar_otra_ventana():
    # Creamos la otra ventana
    otra_ventana = tk.Toplevel()
    otra_ventana.title("Otra ventana")

    # Capturamos el evento de cierre de la ventana
    otra_ventana.protocol("WM_DELETE_WINDOW", mostrar_ventana_principal)

    # Creamos un botón para cerrar la ventana
    boton_cerrar = tk.Button(otra_ventana, text="Cerrar", command=otra_ventana.destroy)
    boton_cerrar.pack()

# Mostramos la ventana principal al ejecutar el programa
mostrar_ventana_principal()