from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
class Graph:
    
    #Inicializa el grafo
    def __init__(objectoActual, arista):
        objectoActual.listaAdya = defaultdict(list)
        for u, v in arista:
            objectoActual.listaAdya[u].append(v)
            objectoActual.listaAdya[v].append(u)

    #Se comprueba que la arista a eliminar no descomponga el grafo, es decir, no separe 
    def validarGrafoNoDescompuesto(objectoActual, u, v):
        if len(objectoActual.listaAdya[u]) == 1:
            return True
        else:
            verticeVisitado = [False] * len(objectoActual.listaAdya)
            contador1 = objectoActual.busquedaProfundidad(u, verticeVisitado)

            objectoActual.eliminarArista(u, v)
            verticeVisitado = [False] * len(objectoActual.listaAdya)
            contador2 = objectoActual.busquedaProfundidad(u, verticeVisitado)

            objectoActual.listaAdya[u].append(v)
            objectoActual.listaAdya[v].append(u)

            return False if contador1 > contador2 else True
    
    #Se elimina la arista por la cual ya se paso
    def eliminarArista(objectoActual, u, v):
        objectoActual.listaAdya[u].remove(v)
        objectoActual.listaAdya[v].remove(u)

    #Se usa el metodo de profundidad para contar la cantidad de vertices al cual puede llegar un vertice
    def busquedaProfundidad(objectoActual, v, verticeVisitado):
        contador = 1
        verticeVisitado[v] = True
        for i in objectoActual.listaAdya[v]:
            if not verticeVisitado[i]:
                contador = contador + objectoActual.busquedaProfundidad(i, verticeVisitado)
        return contador

    """
    Se usa para iniciar desde un vertice cualquiera, moviendose entre los vertices y
    las aristas, mientras elimina estas ultimas.
    """
    def circuitoRecursivo(objectoActual, u, T):
        for v in objectoActual.listaAdya[u]:
            if objectoActual.validarGrafoNoDescompuesto(u, v):
                objectoActual.eliminarArista(u, v)
                objectoActual.circuitoRecursivo(v, T)

        T.append(u)

    #Imprime la ruta del grafo, siempre y cuando sea un circuito 
    def imprimirCircuitoGrafo(objectoActual):
        if not objectoActual.circuitoGrafo():
            print("No se puede realizar la trayectoria en el anterior grafo, puesto que es un camino y no un circuito.")
            return
        u = next(iter(objectoActual.listaAdya))

        T = []
        objectoActual.circuitoRecursivo(u, T)
        print("El circuito es:", T)

    #Validar que el grafo sea conexo 
    def validarConexo(objectoActual):
        verticeVisitado = [False] * len(objectoActual.listaAdya)
        for i in objectoActual.listaAdya:
            if len(objectoActual.listaAdya[i]) > 1:
                break
        else:
            return True

        objectoActual.busquedaProfundidad(next(iter(objectoActual.listaAdya)), verticeVisitado)

        for i in objectoActual.listaAdya:
            if verticeVisitado[i] == False and len(objectoActual.listaAdya[i]) > 0:
                return False
        return True

    #Valida que el grafo tenga un circuito
    def circuitoGrafo(objectoActual):
        if not objectoActual.validarConexo():
            return False
        for i in objectoActual.listaAdya:
            if len(objectoActual.listaAdya[i]) % 2 != 0:
                return False
        return True    
#Ventanas del resultado
class MainWindow:
    def __init__(self, a):
        self.root = tk.Tk()
        self.root.title("Ventana principal")
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.label = tk.Label(self.root, text="Este es el resultado: " + a)
        self.label.pack(padx=20, pady=20)

        self.root.mainloop()

    def on_exit(self):
        self.root.destroy()
        SecondaryWindow()
class SecondaryWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ventana secundaria")

        self.label = tk.Label(self.root, text="Hasta luegooooooooo chao ")
        self.label.pack(padx=20, pady=20)

        self.root.after(3000, self.root.destroy)

        self.root.mainloop()


g2 = Graph([(1, 2), (1,3),(1,4),(1,5),(2,5),(2,4),(2,3),(3,5),(3,4),(4,5)])
#Crear el grafo grafico
G = nx.Graph()
for u, v in g2.listaAdya.items():
    G.add_node(u)
    for i in v:
        G.add_edge(u, i)

#Graficar el grafo
nx.draw(G, with_labels=True)
plt.show()
#Imprimir el circuito hecho
g2.imprimirCircuitoGrafo()