class Node:
    def __init__(self, name):
        self.name = name
        self.list = None


class UnionFind:

    def __init__(self):
        self.lists = []

    def makeSet(self, node):
        new_set = [node]
        node.list = new_set
        self.lists.append(new_set)

    def findSet(self, node):
        return node.list[0]

    def union(self, node, otherNode):
        if self.findSet(node) != self.findSet(otherNode):
            if len(node.list) > len(otherNode.list):
                for i in range(len(otherNode.list)):
                    otherNode.list[i] = node.list
                node.list += otherNode.list
                self.lists.remove(otherNode.list)
            else:
                for i in range(len(node.list)):
                    node.list[i] = otherNode.list
                otherNode.list += node.list
                self.lists.remove(node.list)
