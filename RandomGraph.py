import string 
from random import choice, randint
from collections import defaultdict

class RandomGraph:
    def __init__(self):
        self.letters = string.ascii_uppercase
        self.adjacent_list = defaultdict(list)

class GraphCreation(RandomGraph):
    def __init__(self,nodes):
        self.nodes = nodes
        super().__init__()
    
    def generated_graph(self):
        nodos = list()
        for nod in range(self.nodes):
            nod = choice(self.letters)
            nodos.append(nod)
        return nodos