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
        #self.adjacency_matrix()
           
    def generate_edges(self):
        self.nodos = sorted(sample(self.letters,self.nodes))
        
        for key in self.nodos:
            noditos = self.nodos.copy()
            noditos.remove(key)
            self.adjacent_list[key] = sample(noditos,randint(0,len(noditos)))
            
        return self.adjacent_list
    
    def adjacency_matrix(self):
        graph = self.generate_edges()

        cols = rows = len(self.nodos)

        self.adjacency_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

        for key in self.nodos:
            for neighbor in self.adjacent_list[key]:
                self.edge_list.append((key,neighbor))
        
        for edge in self.edge_list:
            index_of_first_vertex = self.nodos.index(edge[0])
            index_of_second_vertex = self.nodos.index(edge[1])
            self.adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1

        return self.edge_list, self.adjacency_matrix
