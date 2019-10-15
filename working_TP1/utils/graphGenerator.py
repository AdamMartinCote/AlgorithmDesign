import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

BF   = 'Brute force'
DPR  = 'Recursif seuil '
DPR1 = 'Recursif seuil 1'

def graphGenerator(dataBF,dataDpR,dataDpRSeuil,dataNb,seuil):
    plt.ion()
    comparaisonGraph(dataBF,dataDpR,dataDpRSeuil,dataNb,seuil)
    
    #Test de puissance
    puissanceGraph(np.log2(dataNb),np.log2(dataDpRSeuil),DPR+str(seuil))
    puissanceGraph(np.log2(dataNb),np.log2(dataDpR),DPR1)
    puissanceGraph(np.log2(dataNb),np.log2(dataBF),BF)

    #Test de rapport
    # ratioDpRSeuil = genRatioNLogNArray(dataDpRSeuil,dataNb)
    # ratioDpR      = genRatioNLogNArray(dataDpR,dataNb)
    ratioDpRSeuil = genRatioLin(dataDpRSeuil,dataNb)
    ratioDpR      = genRatioLin(dataDpR,dataNb)
    ratioBF       = genRatioExpArray(dataBF,dataNb)
    rapportGraph(dataNb,ratioDpRSeuil,DPR+str(seuil))
    rapportGraph(dataNb,ratioDpR,DPR1)
    rapportGraph(dataNb,ratioBF,BF)

    #Test de constantes
    # fDprSeuil = genNLogNArray(dataNb)
    # fDpr      = genNLogNArray(dataNb)
    fDprSeuil = genLinArray(dataNb)
    fDpr      = genLinArray(dataNb)
    expBF     = genExpArray(dataNb)
    constantesGraph(fDprSeuil,dataDpRSeuil,DPR+str(seuil))
    constantesGraph(fDpr,dataDpR,DPR1)
    plt.ioff()
    constantesGraph(expBF,dataBF,BF)

def comparaisonGraph(dataBF,dataDpR,dataDpRSeuil,dataNb,seuil):
    fig = plt.figure(figsize=(10,10))
    fig.suptitle('Comparaison Algo',fontsize=16)
    ax = fig.add_subplot(111,frameon=True, autoscale_on=True)
    ax.grid(visible=True)
    ax.set_xlabel('Nombre de points')
    ax.set_ylabel('Temps(ms)')
    ax.plot(dataNb,dataBF,'-k',lw=2,label=BF)
    ax.plot(dataNb,dataDpR,'-r',lw=2, label=DPR1)
    ax.plot(dataNb,dataDpRSeuil,'-y',lw=2, label=DPR+str(seuil))
    ax.legend()
    plt.show()

def puissanceGraph(logx,logy,name):
    fig = plt.figure(figsize=(10,10))
    fig.suptitle('Test de puissance '+name,fontsize=16)
    ax = fig.add_subplot(111,frameon=True, autoscale_on=True)
    ax.grid(visible=True)
    ax.set_xlabel('log(Nombre de points)')
    ax.set_ylabel('log(Temps(ms))')
    ax.plot(logx,logy,'-k',lw=2,label=name)
    ax.legend()
    plt.show()

def rapportGraph(x,ratio,name):
    fig = plt.figure(figsize=(10,10))
    fig.suptitle('Test de rapport '+name,fontsize=16)
    ax = fig.add_subplot(111,frameon=True, autoscale_on=True)
    ax.grid(visible=True)
    ax.set_xlabel('Nombre de points')
    ax.set_ylabel('Temps(ms)/f(x)')
    ax.plot(x,ratio,'-k',lw=2,label=name)
    ax.legend()
    plt.show()

def constantesGraph(fx,y,name):
    fig = plt.figure(figsize=(10,10))
    fig.suptitle('Test de constantes '+name,fontsize=16)
    ax = fig.add_subplot(111,frameon=True, autoscale_on=True)
    ax.grid(visible=True)
    ax.set_xlabel('f(x)')
    ax.set_ylabel('Temps(ms)')
    ax.plot(fx,y,'-k',lw=2,label=name)
    ax.legend()
    plt.show()

def genRatioNLogNArray(data,dataNb):
    ratioArray = []
    for nb,val in zip(dataNb,data):
        ratioArray.append(val/(nb*np.log2(nb)))
    return ratioArray

def genRatioExpArray(data,dataNb):
    ratioArray = []
    for nb,val in zip(dataNb,data):
        ratioArray.append(val/nb**2)
    return ratioArray

def genRatioLin(data,dataNb):
    ratioArray = []
    for nb,val in zip(dataNb,data):
        ratioArray.append(val/nb)
    return ratioArray

def genNLogNArray(dataNb):
    nLogNArray = []
    for nb in dataNb:
        nLogNArray.append(nb*np.log2(nb))
    return nLogNArray

def genExpArray(dataNb):
    expArray = []
    for nb in dataNb:
        expArray.append(nb**2)
    return expArray

def genLinArray(dataNb):
    linArray = []
    for nb in dataNb:
        linArray.append(nb)
    return linArray