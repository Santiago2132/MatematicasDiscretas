from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    
    def __init__(self, arista):
        self.listaAdya = defaultdict(list)
        for u, v in arista:
            self.listaAdya[u].append(v)
            self.listaAdya[v].append(u)

    def validarGrafoNoDescompuesto(self, u, v):
        if len(self.listaAdya[u]) == 1:
            return True
        else:
            verticeVisitado = [False] * (max(self.listaAdya.keys()) + 1)
            contador1 = self.busquedaProfundidad(u, verticeVisitado)

            self.eliminarArista(u, v)
            verticeVisitado = [False] * (max(self.listaAdya.keys()) + 1)
            contador2 = self.busquedaProfundidad(u, verticeVisitado)

            self.listaAdya[u].append(v)
            self.listaAdya[v].append(u)

            return False if contador1 > contador2 else True

    def eliminarArista(self, u, v):
        self.listaAdya[u].remove(v)
        self.listaAdya[v].remove(u)

    def busquedaProfundidad(self, v, verticeVisitado):
        contador = 1
        verticeVisitado[v] = True
        for i in self.listaAdya[v]:
            if not verticeVisitado[i]:
                contador = contador + self.busquedaProfundidad(i, verticeVisitado)
        return contador

    def circuitoRecursivo(self, u, T):
        for v in self.listaAdya[u]:
            if self.validarGrafoNoDescompuesto(u, v):
                self.eliminarArista(u, v)
                self.circuitoRecursivo(v, T)

        T.append(u)

    def imprimirCircuitoGrafo(self):
        if not self.circuitoGrafo():
            print("No se puede realizar la trayectoria en el anterior grafo, puesto que es un camino y no un circuito.")
            return
        u = next(iter(self.listaAdya))

        T = []
        self.circuitoRecursivo(u, T)
        print("El circuito es:", T)

    def validarConexo(self):
        verticeVisitado = [False] * (max(self.listaAdya.keys()) + 1)
        for i in self.listaAdya:
            if len(self.listaAdya[i]) > 1:
                break
        else:
            return True

        self.busquedaProfundidad(next(iter(self.listaAdya)), verticeVisitado)

        for i in self.listaAdya:
            if verticeVisitado[i] == False and len(self.listaAdya[i]) > 0:
                return False
        return True

    def circuitoGrafo(self):
        if not self.validarConexo():
            return False
        for i in self.listaAdya:
            if len(self.listaAdya[i]) % 2 != 0:
                return False
        return True    

g1 = Graph([(1, 2),(1,5),(1,4), (1, 3), (2, 3), (3, 5), (3, 4)])
G = nx.Graph()
for u, v in g1.listaAdya.items():
    G.add_node(u)
    for i in v:
        G.add_edge(u, i)

nx.draw(G, with_labels=True)
plt.show()

g1.imprimirCircuitoGrafo()