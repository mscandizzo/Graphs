class MatrixGraph1:
    """Adjacency matrix representation of a graph."""
    def __init__(self, num_vertices):
        self.matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, start_index, end_index):
        """Add an edge from start vertex to end vertex."""
        self.matrix[start_index][end_index] = 1
    

"""Live coding of different ways to represent graphs."""


class Vertex2:
    """MVV - Minimum Viable Vertex."""
    def __init__(self, label):
        self.label = label


class MatrixGraph2:
    """Adjacency matrix representation of a graph."""
    def __init__(self, num_vertices):
        self.matrix = [[0] * num_vertices] * num_vertices
        self.vertices = [Vertex(str(i)) for i in range(num_vertices)]

    def add_edge(self, start_index, end_index, bidirectional=True):
        """Add an edge from start vertex to end vertex."""
        self.matrix[start_index][end_index] = 1
        if bidirectional:
            self.matrix[end_index][start_index] = 1

"""Live coding of different ways to represent graphs."""


class Vertex3:
    """MVV - Minimum Viable Vertex."""
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return str(self.label)


class MatrixGraph3:
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


class Vertex4:
    """Vertices have a label and a set of edges."""
    def __init__(self, label):
        self.label = label
        self.edges = set()

    def __repr__(self):
        return str(self.label)


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
