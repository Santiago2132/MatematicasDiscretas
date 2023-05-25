#Santiago Maldonado Rojas - Manuel Andres Zambrano Pinto
class ConjuntoDisjunto:
    def __init__(self, n):
        """
        Inicialización de la estructura de datos de conjuntos disjuntos
        """
        self.padre = list(range(n)) # El padre de cada elemento es el mismo elemento al inicio
        self.rango = [0] * n # Rango inicial de cada conjunto es 0

    def encontrar(self, x):
        """
        Encuentra el conjunto al que pertenece el elemento x
        """
        if self.padre[x] != x: # Si el padre de x no es x, x no es la raíz del conjunto
            # Aplicamos compresión de camino para optimizar la búsqueda
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        """
        Une los conjuntos de x e y
        """
        # Encontramos los padres de x e y
        px, py = self.encontrar(x), self.encontrar(y)
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
    """
    Implementación del algoritmo de Kruskal para encontrar el árbol de expansión mínimo de un grafo
    """
    n = len(grafo)
    conjuntos = ConjuntoDisjunto(n) # Creamos la estructura de conjuntos disjuntos
    aristas = []
    for i in range(n):
        for j in range(i+1, n):
            if grafo[i][j] != 0:
                # Agregamos las aristas del grafo a una lista, junto con sus pesos y nodos correspondientes
                aristas.append((grafo[i][j], i, j))
    aristas.sort() # Ordenamos las aristas por peso

    arbol_expansion = [] # Inicializamos la lista de aristas del árbol de expansión mínimo
    
    for peso, u, v in aristas:
        if conjuntos.encontrar(u) != conjuntos.encontrar(v): # Si u y v no están en el mismo conjunto
            conjuntos.unir(u, v) # Los unimos en el mismo conjunto
            arbol_expansion.append((u, v, peso)) # Agregamos la arista (u,v) al árbol de expansión mínimo

    return arbol_expansion

def imprimir_grafo_y_arbol(grafo, arbol):
    """
    Función para imprimir el grafo original y el árbol de expansión mínimo
    """
    print("Grafo:")
    for fila in grafo:
        print(fila) # Imprimimos la matriz de adyacencia del grafo
    print("Árbol de expansión mínimo:")
    for u, v, peso in arbol:
        print(f"Nodo {u} -- Nodo {v} : {peso}") # Imprimimos las aristas del árbol de expansión mínimo
    print()
# Ejemplo de uso
grafo2 = [[0,0,8,2,4,0,3],
          [0,0,5,2,0,4,3],
          [8,5,0,0,0,5,2],
          [2,2,0,0,5,0,5],
          [4,0,0,5,0,0,0],
          [0,4,5,0,0,0,0],
          [3,3,2,5,0,0,0]]
arbol_expansion2 = kruskal(grafo2)
imprimir_grafo_y_arbol(grafo2, arbol_expansion2)