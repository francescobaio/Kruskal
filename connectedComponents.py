from unionFind import *


def findConnectedComponents(Graph):

    nodes = [Node(i) for i in range(Graph.shape[0])]
    uf = UnionFind()
    for i in nodes:
        uf.makeSet(i)
    for i in range(Graph.shape[0]):
        for j in range(i+1,Graph.shape[1]):
            if (Graph[i][j] != 0) and (uf.findSet(nodes[i]) != uf.findSet(nodes[j])):
                uf.union(nodes[i],nodes[j])

    print(uf.lists[0])
    return uf
