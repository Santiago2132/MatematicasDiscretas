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
        print(f"{u} -- {v} : {peso}") # Imprimimos las aristas del árbol de expansión mínimo

grafo = [[0, 1, 3, 0],
         [1, 0, 2, 4],
         [3, 2, 0, 5],
         [0, 4, 5, 0]]

arbol_expansion = kruskal(grafo)
imprimir_grafo_y_arbol(grafo, arbol_expansion)