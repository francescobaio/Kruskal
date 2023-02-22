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
    plt.xlabel('Numero dei nodi')
    plt.ylabel('Numero delle componenti connesse')
    plt.savefig('images/numero CC incrementando numero nodi')

    plt.clf()
    plt.cla()
    plt.plot(nodesNumber, time)
    plt.xlabel('numero dei nodi')
    plt.ylabel('tempo in millisecondi')
    plt.savefig('images/tempo findCc incrementando numero nodi')


def testEdgeProbabilityConnectedComponents():
    plt.clf()
    plt.cla()
    nodesNumber = 200
    edgeProbability = np.arange(0, 0.1, 0.001)
    numberConnected = []
    time = []
    for i in range(len(edgeProbability)):
        y = testHelperConnectedComponents(nodesNumber, edgeProbability[i])
        numberConnected.append(y[1])
        time.append(y[0]*1000)
        edgeProbability[i] *= 100
    plt.plot(edgeProbability, time)
    plt.xlabel('Probabilità di presenza degli archi')
    plt.ylabel('tempo in millisecondi')
    plt.savefig('tempo incrementando probabilità')

    plt.clf()
    plt.cla()
    plt.plot(edgeProbability, numberConnected)
    plt.xlabel('probabilità di presenza degli archi')
    plt.ylabel('numero delle componenti connesse')
    plt.savefig('images/numero incrementando probabilità')



def testHelperConnectedComponents(nodesNumber, edgeProbability):
    g = GraphGenerator()
    graph = g.generateGraph(edgeProbability,nodesNumber)
    repetitionNumber = 100
    time = 0
    connectedComponentsNumber = 0
    for j in range(repetitionNumber):
        start = timer()
        cc = findConnectedComponents(graph)
        connectedComponentsNumber += len(cc.lists)
        end = timer()
        time += (end - start)
    return (time / repetitionNumber), (connectedComponentsNumber/repetitionNumber)



def testNodesNumberKruskal():
    plt.clf()
    plt.cla()
    edgeProbability = 0.01
    nodesNumber = range(100, 1000, 10)
    y = []
    for i in range(len(nodesNumber)):
        y.append((testHelperKruskal(nodesNumber[i], edgeProbability))*1000)
    plt.plot(nodesNumber, y)
    plt.xlabel('numero dei nodi')
    plt.ylabel('tempo in millisecondi')
    plt.savefig('images/test_numeroNodi_kruskal')

def testEdgeProbabilityKruskal():
    plt.clf()
    plt.cla()
    nodesNumber = 30
    edgeProbability = np.arange(0, 1, 0.01)
    y = []
    for i in range(len(edgeProbability)):
        y.append((testHelperKruskal(nodesNumber, edgeProbability[i]))*1000)
        edgeProbability[i] *= 100
    plt.plot(edgeProbability, y)
    plt.xlabel('Probabilità archi')
    plt.ylabel('Tempo in millisecondi')
    plt.savefig('images/test_probabilità_kruskal')



def testHelperKruskal(nodesNumber, edgeProbability):
    g = GraphGenerator()
    graph = g.generateWeightedGraph(edgeProbability,nodesNumber)
    time = 0
    for j in range(10):
        k = kruskal(graph)
        start = timer()
        k.kruskal()
        end = timer()
        time += end - start
    return time / 10
