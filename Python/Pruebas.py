import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = np.zeros((num_vertices, num_vertices))

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def remove_edge(self, u, v):
        self.adj_matrix[u][v] = 0
        self.adj_matrix[v][u] = 0

    def is_valid_next_edge(self, u, v):
        # Si el grafo solo tiene una arista, es válida
        if np.sum(self.adj_matrix) == 2:
            return True

        # Contar cuántos nodos están conectados al nodo actual
        degree = np.sum(self.adj_matrix[u])

        # Si el nodo actual tiene más de una arista, es válida
        if degree > 1:
            return True

        # Si el nodo actual tiene solo una arista, eliminarla y ver si el grafo sigue siendo conectado
        self.remove_edge(u, v)
        visited = np.zeros(self.num_vertices)
        self.dfs(u, visited)
        self.add_edge(u, v)

        # Si el grafo sigue siendo conectado, la arista es válida
        if np.sum(visited) == self.num_vertices:
            return True

        return False

    def dfs(self, v, visited):
        visited[v] = 1
        for i in range(self.num_vertices):
            if self.adj_matrix[v][i] == 1 and visited[i] == 0:
                self.dfs(i, visited)

    def fleury(self):
        # Verificar si el grafo es euleriano
        odd_degree_vertices = []
        for i in range(self.num_vertices):
            degree = np.sum(self.adj_matrix[i])
            if degree % 2 == 1:
                odd_degree_vertices.append(i)

        if len(odd_degree_vertices) != 0 and len(odd_degree_vertices) != 2:
            print("El grafo no es euleriano.")
            return []

        # Copiar la matriz de adyacencia para trabajar con ella
        adj_matrix_copy = np.copy(self.adj_matrix)

        # Recorrido de Fleury
        path = []
        if len(odd_degree_vertices) == 0:
            start_vertex = 0
        else:
            start_vertex = odd_degree_vertices[0]

        path.append(start_vertex)

        while np.sum(adj_matrix_copy) > 0:
            current_vertex = path[-1]
            for i in range(self.num_vertices):
                if adj_matrix_copy[current_vertex][i] == 1 and self.is_valid_next_edge(current_vertex, i):
                    path.append(i)
                    adj_matrix_copy[current_vertex][i] = 0
                    adj_matrix_copy[i][current_vertex] = 0
                    break

        return path

    def print_graph(self):
        for i in range(self.num_vertices):
            row = ""
            for j in range(self.num_vertices):
                if self.adj_matrix[i][j] == 1:
                    row += "1 "
                else:
                    row += "0 "
            print(row)

    def print_path(self, path):
        for i in range(len(path) - 1):
            print(str(path[i]) + " -> " + str(path[i+1]))

    def draw_graph(self):
        G = nx.Graph()
        for i in range(self.num_vertices):
            for j in range(i, self.num_vertices):
                if self.adj_matrix[i][j] == 1:
                    G.add_edge(i, j)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_labels(G, pos)
        plt.show()


# Ejemplo de uso
g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.print_graph()
print("Recorrido de Fleury:")
path = g.fleury()
g.print_path(path)

g.draw_graph()