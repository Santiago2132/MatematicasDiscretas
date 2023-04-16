import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
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
                distances[neighbor]['distance'] = distance
                distances[neighbor]['previous'] = current_node
                distances[neighbor]['path'] = distances[current_node]['path'] + [neighbor]
                heapq.heappush(heap, (distances[neighbor]['distance'], neighbor))

    return distances

graph = {
    1: [(2, 4), (3, 2)],
    2: [(1, 4), (3, 1), (4, 5)],
    3: [(1, 2), (2, 1), (4, 8), (5, 10)],
    4: [(2, 5), (3, 8), (5, 2), (6, 6)],
    5: [(3, 10), (4, 2), (6, 3)],
    6: [(4, 6), (5, 3)]
}

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

print(f"Resultados del algoritmo de Dijkstra desde el nodo {start_node}:\n")
for node in distances:
    distance = distances[node]['distance']
    path = distances[node]['path']
    print(f"Distancia desde el nodo {start_node} hasta el nodo {node}: {distance}")
    print(f"Ruta completa desde el nodo {start_node} hasta el nodo {node}: {path}\n")