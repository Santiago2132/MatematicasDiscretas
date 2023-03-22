import tkinter as tk

class InterfazMatriz:
    def __init__(self):
        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.geometry("500x500")#Asignación de tamaño
        self.ventana.title("Matrices 2x2")
        # Bloquear redimensionado
        self.ventana.resizable(False, False)
        # Crear los campos de entrada para la primera matriz
        tk.Label(self.ventana, text="Matriz A:").grid(row=0, column=0, padx=5, pady=5)
        
        self.entry_a11 = tk.Entry(self.ventana, width=5)
        self.entry_a11.grid(row=1, column=0, padx=5, pady=5)
        self.entry_a12 = tk.Entry(self.ventana, width=5)
        self.entry_a12.grid(row=1, column=1, padx=5, pady=5)
        self.entry_a21 = tk.Entry(self.ventana, width=5)
        self.entry_a21.grid(row=2, column=0, padx=5, pady=5)
        self.entry_a22 = tk.Entry(self.ventana, width=5)
        self.entry_a22.grid(row=2, column=1, padx=5, pady=5)

        # Crear un botón para calcular la segunda matriz y mostrarla en una nueva ventana
        tk.Button(self.ventana, text="Calcular matriz B", command=self.calcular_matriz_b).grid(row=3, column=0, padx=60, pady=5)
        
        # Iniciar el bucle principal de la ventana
        self.ventana.mainloop()

    def calcular_matriz_b(self):
        # Obtener los valores de la primera matriz
        a11 = float(self.entry_a11.get())
        a12 = float(self.entry_a12.get())
        a21 = float(self.entry_a21.get())
        a22 = float(self.entry_a22.get())

        # Calcular la segunda matriz
        b11 = a22
        b12 = -a12
        b21 = -a21
        b22 = a11
        
        # Crear una nueva ventana para mostrar la segunda matriz
        ventana_b = tk.Toplevel(self.ventana)
        ventana_b.title("Matriz B")

        # Crear etiquetas para mostrar la segunda matriz
        tk.Label(ventana_b, text="Matriz B:").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(ventana_b, text=str(b11)).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(ventana_b, text=str(b12)).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(ventana_b, text=str(b21)).grid(row=2, column=0, padx=5, pady=5)
        tk.Label(ventana_b, text=str(b22)).grid(row=2, column=1, padx=5, pady=5)

# Crear una instancia de la interfaz
InterfazMatriz()



