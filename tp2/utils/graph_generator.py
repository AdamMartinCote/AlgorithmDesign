from typing import List

import matplotlib.pyplot as plt
import numpy as np

BF = 'Brute force'
DPR = 'Recursif seuil '
DPR1 = 'Recursif seuil 1'

# plot_options = {"lw": 2, "linestyle": "-k", "marker": "o"}


def writeGraph(meanTimes, rollSizes):
    # basicPlot(meanTimes, rollSizes)
    twistPlot(meanTimes,rollSizes)


def basicPlot(meanTimes,rollSizes):
    fig = plt.figure(figsize=(10, 10))
    fig.suptitle('Backtrack', fontsize=16)
    ax = fig.add_subplot(111, frameon=True, autoscale_on=True)
    ax.grid(visible=True)
    ax.set_xlabel('Taille du rouleau')
    ax.set_ylabel('Temps(s)')
    ax.plot(rollSizes, meanTimes, '-k', lw=2, label='Basic Plot')
    ax.legend()
    plt.show()

def twistPlot(meanTimes, rollSizes):
    fig = plt.figure(figsize=(10, 10))
    fig.suptitle('Test des constantes(Polynomiale de deuxième ordre)', fontsize=16)
    ax = fig.add_subplot(111, frameon=True, autoscale_on=True)
    ax.grid(visible=True)
    ax.set_xlabel('f(N*N)')
    ax.set_ylabel('Temps(s)')
    f_n = []
    for t,k in zip(meanTimes,rollSizes):
        f_n.append(k**2)
    ax.plot(f_n, meanTimes, '-k', lw=2, label='Basic Plot')
    ax.legend()
    plt.show()
     

# def puissanceGraph(logx, logy, name):
#     fig = plt.figure(figsize=(10, 10))
#     fig.suptitle('Test de puissance ' + name, fontsize=16)
#     ax = fig.add_subplot(111, frameon=True, autoscale_on=True)
#     ax.grid(visible=True)
#     ax.set_xlabel('log(Nombre de points)')
#     ax.set_ylabel('log(Temps(ms))')
#     # ax.plot(logx, logy, label=name, linestyle="", marker="o")
#     ax.plot(logx, logy, label=name, **plot_options)
#     ax.legend()
#     plt.show()


# def rapportGraph(x, ratio, name):
#     fig = plt.figure(figsize=(10, 10))
#     fig.suptitle('Test de rapport ' + name, fontsize=16)
#     ax = fig.add_subplot(111, frameon=True, autoscale_on=True)
#     ax.grid(visible=True)
#     ax.set_xlabel('Nombre de points')
#     ax.set_ylabel('Temps(ms)/f(x)')
#     ax.plot(x, ratio, label=name, **plot_options)
#     ax.legend()
#     plt.show()


# def constantesGraph(fx, y, name):
#     fig = plt.figure(figsize=(10, 10))
#     fig.suptitle('Test de constantes ' + name, fontsize=16)
#     ax = fig.add_subplot(111, frameon=True, autoscale_on=True)
#     ax.grid(visible=True)
#     ax.set_xlabel('f(x)')
#     ax.set_ylabel('Temps(ms)')
#     ax.plot(fx, y, label=name, **plot_options)
#     ax.legend()
#     plt.show()


# def genRatioNLogNArray(data, dataNb):
#     ratioArray = []
#     for nb, val in zip(dataNb, data):
#         ratioArray.append(val / (nb * np.log2(nb)))
#     return ratioArray


# def genRatioExpArray(data, dataNb, f) -> List[float]:
#     ratioArray = []
#     for nb, val in zip(dataNb, data):
#         ratioArray.append(val / f(nb))
#     return ratioArray


# def genRatioLin(data, dataNb):
#     ratioArray = []
#     for nb, val in zip(dataNb, data):
#         ratioArray.append(val / nb)
#     return ratioArray


# def genNLogNArray(dataNb):
#     nLogNArray = []
#     for nb in dataNb:
#         nLogNArray.append(nb * np.log2(nb))
#     return nLogNArray


# def genExpArray(dataNb):
#     expArray = []
#     for nb in dataNb:
#         expArray.append(nb ** 2)
#     return expArray


# def genLinArray(dataNb):
#     linArray = []
#     for nb in dataNb:
#         linArray.append(nb)
#     return linArray
