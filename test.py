from kruskal import *
from graphGenerator import *
from connectedComponents import *
from matplotlib import pyplot as plt
import matplotlib as mpl
from timeit import default_timer as timer
from statistics import mean

mpl.use("TkAgg")


def testNodesConnectedComponents():
    plt.clf()
    plt.cla()

    edgeProbability = 0.01
    nodesNumber = range(10, 100, 1)
    numberConnected = []
    time = []
    for i in range(len(nodesNumber)):
        y = testHelperConnectedComponents(nodesNumber[i], edgeProbability)
        numberConnected.append(y[1])
        time.append(y[0] * 1000)


    plt.plot(nodesNumber, numberConnected)
    plt.xlabel('numero dei nodi')
    plt.ylabel('numero delle componenti connesse')
    plt.savefig('images/numero incrementando numero nodi')

    plt.clf()
    plt.cla()
    plt.plot(nodesNumber, time)
    plt.xlabel('numero dei nodi')
    plt.ylabel('tempo in millisecondi')
    plt.savefig('images/tempo incrementando numero nodi')


def testHelperConnectedComponents(nodesNumber, edgeProbability):
    g = GraphGenerator()
    graph = g.generateGraph(edgeProbability,nodesNumber)
    repetitionNumber = 50
    time = 0
    connectedComponentsNumber = 0
    for j in range(repetitionNumber):
        start = timer()
        cc = findConnectedComponents(graph)
        connectedComponentsNumber += len(cc.lists)
        end = timer()
        time += (end - start)
    return (time / repetitionNumber), (connectedComponentsNumber/repetitionNumber)


