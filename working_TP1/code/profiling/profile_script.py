from algorithms.bruteforce import execute_brute_force
from algorithms.seuil import execute_DpR
from utils.graphGenerator import graphGenerator
from utils.automaticGen import gen

import utils.text_parser
import glob
import numpy as np


def collectResults():
    dataBF = []
    dataDpR = []
    dataDpRSeuil = []
    dataNb = []
    bfFlag = askBF()
    seuil = askSeuil()
    for nbData in range(1000, 50000, 1000):
        gen(nbData, 3)  # arg1: Nombre de points , arg2: Nombre d'echantillons
        print('\nNumber of data: ', nbData, '\n')
        meanBf, meanDpR, meanDpRSeuil = profileAll(bfFlag, seuil)
        print('\nAverage BF      : ', meanBf)
        print('Average Dpr     : ', meanDpR)
        print('Average DprSeuil: ', meanDpRSeuil, '\n')
        dataBF.append(meanBf)
        dataDpR.append(meanDpR)
        dataDpRSeuil.append(meanDpRSeuil)
        dataNb.append(nbData)
    print('Results:\n')
    print('BF      : ', dataBF)
    print('DpR     : ', dataDpR)
    print('DpRSeuil: ', dataDpRSeuil)
    print('nbData  : ', dataNb)
    writeGraph(dataBF, dataDpR, dataDpRSeuil, dataNb, seuil)


def profileAll(flag, seuil):
    files = getDataFiles()
    if flag:
        bfMean = bfAlgoExecuter(files)
    else:
        bfMean = 1
    DpRMean = dprAlgoExecuter(files, 1)
    DpRMeanSeuil = dprAlgoExecuter(files, seuil)
    return bfMean, DpRMean, DpRMeanSeuil


def getDataFiles():
    bfData = []
    DpRData = []
    path = './code/profiling/data'
    files = None
    try:
        files = glob.glob(path + '/*')
    except:
        print('Path', path, 'not found')
    return files


def dprAlgoExecuter(files, seuil):
    DpRData = []
    for f in files:
        x, y = utils.text_parser.fileToArraySeuilMethod(f)
        DpRTime = execute_DpR(x, y, seuil)
        print('DpR ' + str(seuil) + ' (time): ', DpRTime)
        DpRData.append(DpRTime)
    return np.mean(DpRData)


def bfAlgoExecuter(files):
    bfData = []
    for f in files:
        points = utils.text_parser.fileToArrayBruteMethod(f)
        bfTime = execute_brute_force(points)
        print('BF(time)     : ', bfTime)
        bfData.append(bfTime)
    return np.mean(bfData)


def writeGraph(dataBF, dataDpR, dataDpRSeuil, dataNb, seuil):
    graphGenerator(dataBF, dataDpR, dataDpRSeuil, dataNb, seuil)


def askBF():
    choices = {'y', 'Y', 'n', 'N'}
    choice = None
    while not choice in choices:
        choice = input('Do you want to do brute force too?(it can take a while)[Y/n]: ')
    if choice.lower() == 'y':
        return True
    else:
        return False


def askSeuil():
    choice = None
    while choice == None:
        try:
            choice = int(input('Seuil de recursivite: '))
        except ValueError:
            print('\nLe seuil doit etre un nombre\n')
    return choice
