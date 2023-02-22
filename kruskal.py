from unionFind import *


def sortByKey(edges):
    return edges[2]


def kruskal(Graph):

    nodes = [Node(i) for i in range(Graph.shape[0])]
    uf = UnionFind()
    edges = []
    minimumSpanningTree = []

    for i in nodes:
        uf.makeSet(i)

    for i in range(Graph.shape[0]):
        for j in range(i+1,Graph.shape[1]):
            if Graph[i][j] != 0:
                edges.append((i,j,Graph[i][j]))

    edges.sort(key=sortByKey)
    for edge in edges:
        if uf.findSet(nodes[edge[0]]) != uf.findSet(nodes[edge[1]]):
            uf.union(nodes[edge[0]],nodes[edge[1]])
            minimumSpanningTree.append(edge)


    return minimumSpanningTree




