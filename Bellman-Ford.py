"""
title : Bellman-Ford Algo implementation
author : $1D@1298
date : 11-11-2020
"""
import math

INF = math.inf


class Graph:
    def __init__(self, vertex_count):
        self.V = vertex_count
        self.graph = list()
        """A graph is a collection of vertices and edges. Here we will consider the graph to be a 
        collection (list) of edges. Each edge is a list containing information of starting vertex (u), ending vertex (v)
        and weight (w) of the edge respectively."""

    def insert_edge(self, u, v, w):
        """
        Adds an edge to the graph (self.graph). Each edge is represented as a list within the graph
        :param u: starting vertex of the edge (edge is outgoing here)
        :param v: ending vertex of the edge (edge is incoming here)
        :param w: weight of the vertex going from u to v
        """
        self.graph.append([u, v, w])

    def print_distance(self, distances):
        print("Vertex\t\tDistance")
        for i in range(self.V):
            print(f"{i}\t\t\t{distances[i]}")

    def get_source(self, source):
        pass

    def relax(self, source):
        """
        Relaxes the edges and finds negative weighted cycles
        :param source: Source vertex for the graph
        """

        # Initializing the distances of all vertices as infinite
        distances = [INF] * self.V
        distances[source] = 0

        # Relaxing the edges |V|-1 ie. n-1 times
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distances[u] != INF and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        # Checking of negative weighted cycles, if relaxation is still possible, then a negative weighted cycle will
        # exist
        for u, v, w in self.graph:
            if distances[u] != INF and distances[u] + w < distances[v]:
                print("Graph contains a negative weighted cycle")

        self.print_distance(distances)


n = eval(input("Enter number of vertices: "))
source = eval(input("Enter source vertex: "))
g = Graph(n)
add_edge = True
print("Please add edges \nu is source vertex of the edge \nv is destination vertex of the edge \nw is weight of the "
      "edge: ")
while add_edge:
    g.insert_edge(eval(input("u: ")), eval(input("v: ")), eval(input("w: ")))
    add_edge = bool(input("Would you like to add an edge? \n(Enter anything to add an edge. \nLeave empty to stop): "))
print(g.graph)
g.relax(source)
