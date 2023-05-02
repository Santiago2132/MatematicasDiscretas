import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import heapq

class CubeGraph:
    def __init__(self, nx, ny, nz):
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.vertices = []
        self.edges = {}
        self._build_graph()

    def _build_graph(self):
        # Add vertices
        for x in range(self.nx):
            for y in range(self.ny):
                for z in range(self.nz):
                    vertex = (x, y, z)
                    self.vertices.append(vertex)
                    self.edges[vertex] = []

        # Add edges
        for vertex in self.vertices:
            x, y, z = vertex
            if x > 0:
                neighbor = (x-1, y, z)
                self.edges[vertex].append((neighbor, 1))
            if x < self.nx - 1:
                neighbor = (x+1, y, z)
                self.edges[vertex].append((neighbor, 1))
            if y > 0:
                neighbor = (x, y-1, z)
                self.edges[vertex].append((neighbor, 1))
            if y < self.ny - 1:
                neighbor = (x, y+1, z)
                self.edges[vertex].append((neighbor, 1))
            if z > 0:
                neighbor = (x, y, z-1)
                self.edges[vertex].append((neighbor, 1))
            if z < self.nz - 1:
                neighbor = (x, y, z+1)
                self.edges[vertex].append((neighbor, 1))

    def shortest_path(self, start, end):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            (current_distance, current_vertex) = heapq.heappop(heap)
            if current_distance > distances[current_vertex]:
                continue
            if current_vertex == end:
                return distances[end]
            for (neighbor, distance) in self.edges[current_vertex]:
                distance_to_neighbor = current_distance + distance
                if distance_to_neighbor < distances[neighbor]:
                    distances[neighbor] = distance_to_neighbor
                    heapq.heappush(heap, (distance_to_neighbor, neighbor))
        return None
#Funcion grafica
def plot_cube_graph(graph):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Dibujar los vértices
    xs, ys, zs = zip(*graph.vertices)
    ax.scatter(xs, ys, zs)

    # Dibujar los bordes
    for vertex, edges in graph.edges.items():
        x1, y1, z1 = vertex
        for (x2, y2, z2), _ in edges:
            ax.plot([x1, x2], [y1, y2], [z1, z2], 'k-')

    # Configurar el gráfico
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()
# Crear un cubo de 2x2x2 y encontrar el camino más corto entre dos vértices
graph = CubeGraph(1, 1, 1)
start = (0, 0, 0)
end = (1, 1, 1)
shortest_distance = graph.shortest_path(start, end)
#plot_cube_graph(graph)
print(f"Shortest distance from {start} to {end}: {shortest_distance}")