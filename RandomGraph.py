import string 
from random import randint, sample
from collections import defaultdict

class RandomGraph:
    def __init__(self):
        self.letters = string.ascii_uppercase
        self.adjacent_list = defaultdict()
        self.nodos = list()
        self.edge_list = list()
        
class GraphCreation(RandomGraph):
    def __init__(self,nodes):
        self.nodes = nodes
        super().__init__()
           
    def generate_edges(self):
        self.nodos = sample(self.letters,self.nodes)
        
        for key in self.nodos:
            noditos = self.nodos.copy()
            noditos.remove(key)
            self.adjacent_list[key] = sample(noditos,randint(0,len(noditos)))
            
        return self.adjacent_list
    
    def adjacency_matrix(self):
        graph = self.generate_edges()

        matrix_elements = sorted(graph.keys())
        cols = rows = len(matrix_elements)

        adjacency_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

        for key in matrix_elements:
            for neighbor in graph[key]:
                self.edge_list.append((key,neighbor))
        
        for edge in self.edge_list:
            index_of_first_vertex = matrix_elements.index(edge[0])
            index_of_second_vertex = matrix_elements.index(edge[1])
            adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

        return matrix_elements, self.edge_list, adjacency_matrix