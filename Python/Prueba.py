import heapq
import networkx as nx
import matplotlib.pyplot as plt
def dijkstra(graph, start):
    """
    Implementación del algoritmo de Dijkstra para encontrar el camino más corto
    desde un nodo origen a todos los demás nodos en un grafo ponderado.

    :param graph: Grafo representado como un diccionario de listas de adyacencia.
                  Cada llave representa un nodo y su valor es una lista de tuplas
                  (nodo_destino, peso) que representan las aristas que salen del nodo.
    :param start: Nodo origen para calcular los caminos más cortos.
    :return: Diccionario con la información de los caminos más cortos desde el nodo origen.
             Cada llave representa un nodo y su valor es un diccionario con las siguientes llaves:
             - 'distance': distancia desde el nodo origen al nodo actual.
             - 'previous': nodo previo en el camino más corto.
             - 'path': ruta completa desde el nodo origen hasta el nodo actual.
    """
    distances = {node: {'distance': float('inf'), 'previous': None, 'path': []} for node in graph}
    distances[start]['distance'] = 0
    distances[start]['path'] = [start]

    heap = [(0, start)]
    while heap:
        (current_distance, current_node) = heapq.heappop(heap)

        if current_distance > distances[current_node]['distance']:
            continue

        for (neighbor, weight) in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]['distance']:
                distances[neighbor]['distance'] = distance + abs(current_node - neighbor)
                distances[neighbor]['previous'] = current_node
                distances[neighbor]['path'] = distances[current_node]['path'] + [neighbor]
                heapq.heappush(heap, (distances[neighbor]['distance'], neighbor))

    return distances

'''
graph = {
    1: [(2, 2), (3, 1)],
    2: [(1, 2), (3, 2)],
    3: [(1, 1), (2, 2)]
}
'''

graph= {
    1: [(2,4),(3,2)],
    2: [(1,4),(3,1,),(4,5)],
    3: [(1,2),(2,1),(4,8),(5,10)],
    4: [(2,5),(3,8),(5,2),(6,6)],
    5: [(3,10),(4,2),(6,3)],
    6: [(4,6),(5,3)]
}
#Impresión del grafo
G = nx.DiGraph()

for node in graph:
    G.add_node(node)

for node in graph:
    for edge in graph[node]:
        G.add_edge(node, edge[0], weight=edge[1])

pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_edges(G, pos, edge_color='gray')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=16, font_family='sans-serif')
plt.axis('off')
plt.show()


start_node = 1

distances = dijkstra(graph, start_node)

total_cost = distances[start_node]['distance']
path = distances[start_node]['path']

print(f"La ruta completa desde el nodo {start_node} es {path}")
print(f"El costo total del recorrido es {total_cost}")

for node in distances:
    if node != start_node:
        distance = distances[node]['distance']
        path = distances[node]['path']
        print(f"Distancia desde el nodo {start_node} hasta el nodo {node}: {distance}")
        print(f"Ruta completa desde el nodo {start_node} hasta el nodo {node}: {path}")

        if node == start_node:
            print(f"El costo total del recorrido es {distance}")
            print(f"La ruta completa desde el nodo {start_node} hasta el nodo {node} es {path}")