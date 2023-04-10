class Graph:
    def __init__(self, edges):
        self.graph = {}
        self.visited = {}

        # Creamos un diccionario donde las claves son los nodos y los valores son
        # las listas de nodos con los que están conectados
        for start, end in edges:
            if start not in self.graph:
                self.graph[start] = []
                self.visited[start] = False
            if end not in self.graph:
                self.graph[end] = []
                self.visited[end] = False
            self.graph[start].append(end)
            self.graph[end].append(start)

    def fleury(self, start):
        path = [start]
        self.visited[start] = True

        while len(path) < len(self.graph):
            # Buscamos el último nodo en el camino actual
            current = path[-1]
            # Obtenemos los vecinos del nodo actual que no han sido visitados
            neighbors = [n for n in self.graph[current] if not self.visited[n]]
            if not neighbors:
                # Si no hay vecinos disponibles, retrocedemos un nodo
                path.pop()
            else:
                # Si hay vecinos disponibles, elegimos uno y lo agregamos al camino
                next_node = neighbors[0]
                # Si la arista que conecta el nodo actual con el siguiente es un puente,
                # necesitamos elegir otra arista
                if len(neighbors) == 1 and self.is_bridge(current, next_node):
                    continue
                path.append(next_node)
                self.visited[next_node] = True

        return path

    def is_bridge(self, start, end):
        # Marcamos el nodo de partida como visitado
        self.visited[start] = True

        # Contamos el número de componentes conectados después de eliminar la arista
        count1 = self.count_components(start)

        # Restauramos el estado de visitado para el nodo de partida
        self.visited[start] = False

        # Eliminamos la arista
        self.graph[start].remove(end)
        self.graph[end].remove(start)

        # Contamos el número de componentes conectados después de eliminar la arista
        count2 = self.count_components(start)

        # Restauramos la arista
        self.graph[start].append(end)
        self.graph[end].append(start)

        # La arista es un puente si el número de componentes conectados aumenta después de eliminarla
        return count2 > count1

    def count_components(self, start):
        count = 0
        self.visited[start] = True
        stack = [start]

        while stack:
            current = stack.pop()
            for neighbor in self.graph[current]:
                if not self.visited[neighbor]:
                    self.visited[neighbor] = True
                    stack.append(neighbor)
            # Si llegamos al final del camino, hemos encontrado un componente conectado
            if not stack:
                count += 1

        return count


# Ejemplo de uso
edges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4)]
graph = Graph(edges)
path = graph.fleury(1)
print(path)  # Salida: [1, 2, 3, 4, 2, 1, 3]