from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import  tkinter as tk
class Graph:
    def __init__(self, edges):
        self.adj_list = defaultdict(list)
        for u, v in edges:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def remove_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def DFS_count(self, v, visited):
        count = 1
        visited[v] = True
        for i in self.adj_list[v]:
            if not visited[i]:
                count = count + self.DFS_count(i, visited)
        return count

    def is_valid_next_edge(self, u, v):
        if len(self.adj_list[u]) == 1:
            return True
        else:
            visited = [False] * len(self.adj_list)
            count1 = self.DFS_count(u, visited)

            self.remove_edge(u, v)
            visited = [False] * len(self.adj_list)
            count2 = self.DFS_count(u, visited)

            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

            return False if count1 > count2 else True
        
    def print_euler_util(self, u, T):
        for v in self.adj_list[u]:
            if self.is_valid_next_edge(u, v):
                self.remove_edge(u, v)
                self.print_euler_util(v, T)

        T.append(u)
        
    def print_euler_tour(self):
        if not self.is_eulerian_circuit():
            print("No se puede realizar la trayectoria en el anterior grafo.")
            return
        u = next(iter(self.adj_list))

        T = []
        self.print_euler_util(u, T)
        print("El circuito es:", T)

    def is_connected(self):
        visited = [False] * len(self.adj_list)
        for i in self.adj_list:
            if len(self.adj_list[i]) > 1:
                break
        else:
            return True

        self.DFS_count(next(iter(self.adj_list)), visited)

        for i in self.adj_list:
            if visited[i] == False and len(self.adj_list[i]) > 0:
                return False
        return True

    def is_eulerian_circuit(self):
        if not self.is_connected():
            return False
        for i in self.adj_list:
            if len(self.adj_list[i]) % 2 != 0:
                return False
        return True

    def draw_graph(self):
        G = nx.Graph()
        for u in self.adj_list:
            for v in self.adj_list[u]:
                G.add_edge(u, v)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        plt.show()
#Ventanas
class MainWindow:
    def __init__(self,a):
        self.root = tk.Tk()
        self.root.title("Ventana principal")
        self.root.protocol("WM_DELETE_WINDOW", self.on_exit)

        self.label = tk.Label(self.root, text="Este es el resultado: "+a)
        self.label.pack(padx=20, pady=20)

        self.root.mainloop()

    def on_exit(self):
        self.root.destroy()
        SecondaryWindow()

class SecondaryWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ventana secundaria")

        self.label = tk.Label(self.root, text="Hasta luegooooooooo chao ")
        self.label.pack(padx=20, pady=20)

        self.root.after(5000, self.root.destroy)

        self.root.mainloop()

MainWindow("Santiago")
g1 = Graph([(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (4, 5), (5, 6), (6, 4), (4, 7), (7, 3), (3, 2), (2, 1), (1, 0)])
g1.draw_graph()
g1.print_euler_tour()
