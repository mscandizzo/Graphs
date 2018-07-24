from collections import deque

class Vertex:
    """Vertices have a label and a set of edges."""

    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)
    
    def list_to_matrix(dictionary):
        edge_list = []
        for key in dictionary:
            for neighbor in dictionary[key]:
                edge_list.append((key,neighbor))
        return edge_list

class MatrixGraph:
    """Adjacency matrix representation of a graph."""

    def __init__(self, num_vertices):
        self.matrix = [[0 for _ in range(num_vertices)]
                       for _ in range(num_vertices)]
        self.vertices = [Vertex(str(i)) for i in range(num_vertices)]

    def add_edge(self, start_index, end_index, bidirectional=True):
        """Add an edge from start vertex to end vertex."""
        self.matrix[start_index][end_index] = 1
        if bidirectional:
            self.matrix[end_index][start_index] = 1

            """Graph representation using adjacency list."""

class ListGraph4:
    """Adjacency list graph."""

    def __init__(self):
        self.vertices = set()

    def add_edge(self, start, end, bidirectional=True):
        """Add an edge from start to end."""
        if start not in self.vertices or end not in self.vertices:
            raise Exception('Error - vertices not in graph!')
        start.edges.add(end)
        if bidirectional:
            end.edges.add(start)

    def add_vertex(self, vertex):
        if not hasattr(vertex, 'label'):
            raise Exception('This is not a vertex!')
        self.vertices.add(vertex)

    def breadth_first_search(graph, root):
        visited_vertices = list()
        graph_queue = deque([root])
        visited_vertices.append(root)
        node = root

        while len(graph_queue)>0:
            node = graph_queue.popleft()
            adj_nodes = graph[node]
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
            if len(remaining_elements) > 0:
                for elem in sorted(remaining_elements):
                    visited_vertices.append(elem)
                    graph_queue.append(elem)
        
        return visited_vertices

    def depth_first_search(graph, root):
        visited_vertices = list()
        graph_stack = list()

        graph_stack.append(root)
        node = root

        while len(graph_stack) > 0:
            if node not in visited_vertices:
                visited_vertices.append(node)
            adj_nodes = graph[node]
            if set(adj_nodes).issubset(set(visited_vertices)):
                graph_stack.pop()
            if len(graph_stack) >0:
                node = graph_stack[-1]
                continue
            else:
                remaining_elements = set(adj_nodes).difference(set(visited_vertices))

            first_adj_node = sorted(remaining_elements)[0]
            graph_stack.append(first_adj_node)
            node = first_adj_node
        return visited_vertices

