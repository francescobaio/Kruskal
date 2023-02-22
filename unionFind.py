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

        tmp = otherNode.list
        ptr = node.list

        if self.findSet(node) != self.findSet(otherNode):
            if len(node.list) > len(otherNode.list):
                for i in range(len(otherNode.list)):
                    tmp[i].list = node.list
                node.list += tmp
                self.lists.remove(tmp)
            else:
                for i in range(len(node.list)):
                    ptr[i].list = otherNode.list
                otherNode.list += ptr
                self.lists.remove(ptr)
