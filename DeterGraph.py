from collections import defaultdict

class GraphCreation:
    def __init__(self):
        self.adjacent_list = defaultdict()
        self.nodos = list()
        self.edge_list = list()
        
        
    def add_nodes_to_edge(self,key,list_of_edges):
        self.adjacent_list[key] = list_of_edges

    def building_nodos(self):
        lista = list()
        for key in self.adjacent_list:
            lista.append(key)
            for neighbor in self.adjacent_list[key]:
                lista.append(neighbor)
        self.nodos = list(set(lista))

        return self.nodos

    
    def adjacency_matrix(self):
        
        self.building_nodos()

        cols = rows = len(self.nodos)

        self.adjacency_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

        for key in self.nodos:
            for neighbor in self.adjacent_list[key]:
                self.edge_list.append((key, neighbor))

        for edge in self.edge_list:
            index_of_first_vertex = self.nodos.index(edge[0])
            index_of_second_vertex = self.nodos.index(edge[1])
            self.adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

        return self.adjacency_matrix
