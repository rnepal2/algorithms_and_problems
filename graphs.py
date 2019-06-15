import math
import numpy
import random

# graph vertex/node
class Vertex:
    
    def __init__(self, name):
        self.name = name  # vetex name
        self.neighbors = []
    
    # prints a vertex
    def print_vertex(self):
        print('\nvertex: ', self.name, end='')
        if self.neighbors:
            print(' neighbors: ', end='')
            for neighbor in self.neighbors:
                print(neighbor.name, end=' ')
        print('')
        
# the graph class    
class Graph:
    
    def __init__(self):
        self.vertices = []
    
    # adds a vertex to the graph
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            if vertex not in self.vertices:
                self.vertices.append(vertex)
                #print('vertex ', vertex.name, ' added.')
    
    # adds an edge joining vertex1 and vertex2 to the graph
    def add_edge(self, vertex1, vertex2):
        # Undirected/bidirected graph
        if isinstance(vertex1, Vertex) and isinstance(vertex2, Vertex):
            vertex1.neighbors.append(vertex2)
            vertex2.neighbors.append(vertex1)
            #print('an edge ', vertex1.name + vertex2.name, ' added.')
            
    def breadth_search(self, start_vertex, find_vertex):
        print('begining vertex: ', start_vertex.name)
        explored = []
        frontiers = [start_vertex]
        
        while frontiers:
            node = frontiers.pop(0)
            if node not in explored:
                explored.append(node)
                for neighbor in node.neighbors:
                    frontiers.append(neighbor)
        return explored
   
    # print the current graph
    def print_graph(self):
        print('the graph is: ')
        for vertex in self.vertices:
            vertex.print_vertex()


seed = random.randint(0, 10000)
random.seed(seed)
vertex_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
random.shuffle(vertex_names)

vertices = []
for i in range(9):
    vertex_ = vertex_names[i]
    vertex = 'vertex' + '%d'.format(i)
    vertex = Vertex(vertex_)
    vertices.append(vertex)
    
graph = Graph()
for vertex in vertices:
    graph.add_vertex(vertex)

# how many edges to add, n = 10?
for i in range(10):
    rand1 = random.randint(0, len(vertices)-1)
    rand2 = random.randint(0, len(vertices)-1)
    if rand1 != rand2:
        vertex1 = vertices[rand1]; vertex2 = vertices[rand2]
        if vertex1 not in vertex2.neighbors:
            #if vertex2 not in vertex1.neighbors:
            graph.add_edge(vertices[rand1], vertices[rand2])

graph.print_graph()

explored = graph.breadth_search(vertices[1], vertices[7])
print('nodes explored: ')
for node in explored:
    print(node.name, end=', ')
print('')