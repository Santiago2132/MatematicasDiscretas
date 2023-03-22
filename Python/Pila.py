import tkinter as tk
import numpy as np

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Matriz 3x3")
        self.matrix = np.zeros((3, 3))
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                entry = tk.Entry(self, width=5)
                entry.grid(row=i, column=j)
                self.matrix[i][j] = tk.IntVar()
                entry.configure(textvariable=self.matrix[i][j])

        button = tk.Button(self, text="Imprimir", command=self.print_matrix)
        button.grid(row=3, column=1)

    def print_matrix(self):
        print(self.matrix)


if __name__ == '__main__':
    window = Window()