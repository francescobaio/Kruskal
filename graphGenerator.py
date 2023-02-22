import random

import numpy as np


class GraphGenerator:

    def generateGraph(self, probability, size):
        adjMatrix = np.zeros((size, size))
        for i in range(size):
            for j in range(i + 1, size):
                if np.random.rand() < probability:
                    adjMatrix[i][j] = 1
                    adjMatrix[j][i] = 1

        return adjMatrix

    def generateWeightedGraph(self, probability, size):
        adjMatrix = np.zeros((size, size))
        for i in range(size):
            for j in range(i + 1, size):
                if np.random.rand() < probability:
                    adjMatrix[i][j] = random.randint(1, 10)
                    adjMatrix[j][i] = adjMatrix[i][j]

        return adjMatrix