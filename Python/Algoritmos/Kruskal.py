class ConjuntoDisjunto:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        px, py = self.encontrar(x), self.encontrar(y)
        if px == py:
            return
        if self.rango[px] < self.rango[py]:
            self.padre[px] = py
        elif self.rango[px] > self.rango[py]:
            self.padre[py] = px
        else:
            self.padre[py] = px
            self.rango[px] += 1

def kruskal(grafo):
    n = len(grafo)
    conjuntos = ConjuntoDisjunto(n)
    aristas = []
    for i in range(n):
        for j in range(i+1, n):
            if grafo[i][j] != 0:
                aristas.append((grafo[i][j], i, j))
    aristas.sort()

    arbol_expansion = []
    for peso, u, v in aristas:
        if conjuntos.encontrar(u) != conjuntos.encontrar(v):
            conjuntos.unir(u, v)
            arbol_expansion.append((u, v, peso))

    return arbol_expansion