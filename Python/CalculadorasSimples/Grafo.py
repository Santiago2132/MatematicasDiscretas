from collections import defaultdict
class Graph:
#Manuel Andres Zambrano Pinto - Santiago Maldonado Rojas
    # Método para inicializar el grafo
    def __init__(self, aristas):
        # Crear un diccionario de listas para almacenar la lista de adyacencia del grafo
        self.lista_ady = defaultdict(list)
        # Recorrer la lista de aristas y agregarlas a la lista de adyacencia
        for u, v in aristas:
            # Agregar el vértice v a la lista de adyacencia del vértice u
            self.lista_ady[u].append(v)
            # Agregar el vértice u a la lista de adyacencia del vértice v
            self.lista_ady[v].append(u)

    # Método de busqueda en profundidad
    def busqueda_camino_vertices(self, v, visitados):
        # Marcar el vértice actual como visitado
        visitados[v] = True
        # Recorrer todos los vértices adyacentes al vértice actual
        for u in self.lista_ady[v]:
            # Si un vértice adyacente no ha sido visitado, llamar al método DFS recursivamente
            if not visitados[u]:
                self.busqueda_camino_vertices(u, visitados)

    # Método de conexo
    def es_conexo(self):
        # Crear un diccionario de booleanos para almacenar si cada vértice ha sido visitado o no
        visitados = {v: False for v in self.lista_ady}
        # Empezar el recorrido DFS desde el primer vértice de la lista de adyacencia
        self.busqueda_camino_vertices(next(iter(self.lista_ady)), visitados)
        # Si hay algún vértice que no ha sido visitado, el grafo no es conexo
        return all(visitados.values())

    # Método para verificar si es euleriano
    def es_euleriano(self):
        # Verificar si el grafo es conexo
        if not self.es_conexo():
            return False
        # Verificar si cada vértice tiene grado par
        for v in self.lista_ady:
            # Si el grado del vértice actual no es par, el grafo no es euleriano
            if len(self.lista_ady[v]) % 2 != 0:
                return False
        # Si todos los vértices tienen grado par, el grafo es euleriano
        return True

    # Busca el circuito en el grafo
    def circuito_euleriano(self):
        # Verifica si el grafo es euleriano antes de continuar
        if not self.es_euleriano():
            # Si no es euleriano, retorna None
            return None
        circuito = []
        # Crea una pila con un vértice arbitrario
        pila = [next(iter(self.lista_ady))]
        while pila:
            # Toma el último vértice agregado a la pila
            v = pila[-1]
            if self.lista_ady[v]:
                # Si el vértice tiene adyacentes, toma uno y lo elimina de la lista de adyacencia
                u = self.lista_ady[v].pop()
                self.lista_ady[u].remove(v)
                # Agrega el nuevo vértice a la pila
                pila.append(u)
            else:
                # Si no hay más adyacentes para el vértice actual, lo agrega al circuito
                circuito.append(pila.pop())
        # Retorna el circuito euleriano encontrado
        return circuito

    # Método para imprimir el circuito 
    def imprimir_circuito_euleriano(self):
        # Obtiene el circuito euleriano del grafo
        circuito = self.circuito_euleriano()
        if circuito is None:
            # Si no se puede obtener un circuito euleriano, imprime un mensaje de error
            print("No se puede realizar la trayectoria en el grafo, puesto que es un camino y no un circuito.")
        else:
            # Si se obtiene un circuito euleriano, lo imprime en orden inverso
            print("El circuito es:", circuito[::-1])


g1 = Graph([(1, 2),(1, 5),(1, 4), (1, 3), (2, 3), (3, 5), (3, 4)])

g1.imprimir_circuito_euleriano()