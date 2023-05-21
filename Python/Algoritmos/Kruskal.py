#Santiago Maldonado Rojas - Manuel Andrés Zambrano Pinto - Nelson Yair 
import networkx as nx
import matplotlib.pyplot as plt

class ConjuntoDisjunto:
    def __init__(self, n):
        # Inicialización de la estructura de datos de conjuntos disjuntos
        self.padre = list(range(n)) # El padre de cada elemento es el mismo elemento al inicio
        self.rango = [0] * n # Rango inicial de cada conjunto es 0

    def encontrar(self, x):
        # Encuentra el conjunto al que pertenece el elemento x
        if self.padre[x] != x: # Si el padre de x no es x, x no es la raíz del conjunto
            self.padre[x] = self.encontrar(self.padre[x]) # Aplicamos compresión de camino para optimizar la búsqueda
        return self.padre[x]

    def unir(self, x, y):
        # Une los conjuntos de x e y
        px, py = self.encontrar(x), self.encontrar(y) # Encontramos los padres de x e y
        if px == py: # Si ya están en el mismo conjunto, no hacemos nada
            return
        if self.rango[px] < self.rango[py]: # Si el rango de px es menor al de py, unimos px a py
            self.padre[px] = py
        elif self.rango[px] > self.rango[py]: # Si el rango de px es mayor al de py, unimos py a px
            self.padre[py] = px
        else: # Si los rangos son iguales, podemos unir cualquier conjunto a otro, en este caso elegimos unir py a px
            self.padre[py] = px
            self.rango[px] += 1 # El rango del conjunto resultante se incrementa en 1

def kruskal(grafo):
    n = len(grafo)
    conjuntos = ConjuntoDisjunto(n) # Creamos la estructura de conjuntos disjuntos
    aristas = []
    for i in range(n):
        for j in range(i+1, n):
            if grafo[i][j] != 0:
                aristas.append((grafo[i][j], i, j)) # Agregamos las aristas del grafo a una lista
    aristas.sort() # Ordenamos las aristas por peso

    arbol_expansion = [] # Inicializamos la lista de aristas del árbol de expansión mínimo
    
    for peso, u, v in aristas:
        if conjuntos.encontrar(u) != conjuntos.encontrar(v): # Si u y v no están en el mismo conjunto
            conjuntos.unir(u, v) # Los unimos en el mismo conjunto
            arbol_expansion.append((u, v, peso)) # Agregamos la arista (u,v) al árbol de expansión mínimo

    return arbol_expansion

def imprimir_grafo_y_arbol(grafo, arbol):
    print("Grafo:")
    for fila in grafo:
        print(fila) # Imprimimos la matriz de adyacencia del grafo
    print("Árbol de expansión mínimo:")
    for u, v, peso in arbol:
        print(f"Nodo {u} -- Nodo {v} : {peso}") # Imprimimos las aristas del árbol de expansión mínimo
    print()
        
#Funciones de manera grafica 
def visualizar_grafo(grafo):
    G = nx.Graph() # Creamos un grafo vacío
    n = len(grafo)
    for i in range(n):
        G.add_node(i) # Agregamos un nodo por cada vértice del grafo
        for j in range(i+1, n):
            if grafo[i][j] != 0:
                G.add_edge(i, j, weight=grafo[i][j]) # Agregamos una arista por cada arista del grafo, con su peso correspondiente

    pos = nx.spring_layout(G) # Calculamos la posición de los nodos usando el algoritmo de Fruchterman-Reingold
    labels = {(i,j): grafo[i][j] for (i,j) in G.edges()} # Creamos un diccionario de etiquetas para las aristas

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500) # Dibujamos los nodos
    nx.draw_networkx_labels(G, pos) # Dibujamos las etiquetas de los nodos
    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray') # Dibujamos las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=14) # Dibujamos las etiquetas de las aristas

    plt.axis('off') # Ocultamos los ejes
    plt.show() # Mostramos el grafo

def visualizar_arbol(grafo, arbol):
    G = nx.Graph() # Creamos un grafo vacío
    n = len(grafo)
    for i in range(n):
        G.add_node(i) # Agregamos un nodo por cada vértice del grafo
    for u, v, peso in arbol:
        G.add_edge(u, v, weight=peso) # Agregamos una arista por cada arista del árbol de expansión mínimo, con su peso correspondiente

    pos = nx.spring_layout(G) # Calculamos la posición de los nodos usando el algoritmo de Fruchterman-Reingold
    labels = {(u,v): peso for (u,v,peso) in G.edges(data='weight')} # Creamos un diccionario de etiquetas para las aristas

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500) # Dibujamos los nodos
    nx.draw_networkx_labels(G, pos) # Dibujamos las etiquetas de los nodos
    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray') # Dibujamos las aristas
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=14) # Dibujamos las etiquetas de las aristas

    plt.axis('off') # Ocultamos los ejes
    plt.show() # Mostramos el grafo
    

#grafo2 = [[0,0,2,2,4,0,3],[0,0,6,7,0,4,3],[2,6,0,0,0,5,2],[2,7,0,0,5,0,6],[4,0,0,5,0,0,0],[0,4,5,0,0,0,0],[3,3,2,6,0,0,0,0]]
grafo2 = [[0,0,8,2,4,0,3],[0,0,5,2,0,4,3],[8,5,0,0,0,5,2],[2,2,0,0,5,0,5],[4,0,0,5,0,0,0],[0,4,5,0,0,0,0],[3,3,2,5,0,0,0]]
#grafo2 = [[0,0,7,2,4,0,3],          [0,0,2,4,0,4,3],          [7,2,0,0,0,5,2],          [2,4,0,0,5,0,2],          [4,0,0,5,0,0,0],          [0,4,5,0,0,0,0],          [3,3,2,2,0,0,0]]
#visualizar_grafo(grafo2)
arbol_expansion2 = kruskal(grafo2)
#visualizar_arbol(grafo2,arbol_expansion2)
imprimir_grafo_y_arbol(grafo2, arbol_expansion2)