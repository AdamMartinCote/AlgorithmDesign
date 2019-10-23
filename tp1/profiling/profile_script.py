import glob
from typing import List, Dict

import os
import numpy as np

import utils.text_parser
from algorithms.bruteforce import execute_brute_force
from algorithms.seuil import execute_DpR
from utils.automaticGen import gen
from utils.graphGenerator import genRatioExpArray, rapportGraph
from utils.graphGenerator import graphGenerator
from utils.graphGenerator import puissanceGraph
from utils.text_parser import parse_exemplaire_filepath_to_list

start_at = 1
assay_number = 10
step = 1000


def collectResults():
    dataBF = []
    dataDpR = []
    dataDpRSeuil = []
    dataNb = []
    bfFlag = askBF()
    seuil = askSeuil()
    for nbData in range(start_at * step, assay_number * step, step):
        gen(nbData, 3)  # arg1: Nombre de points , arg2: Nombre d'echantillons
        print('\nNumber of data: ', nbData, '\n')
        meanBf, meanDpR, meanDpRSeuil = profile_all_for_given_size(bfFlag, seuil)
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


def profile_brute_force():
    filepath_list: List[str] = get_filepath_list_from_directory_path()
    exemplaires_list: List[(int, int,)] = [
        parse_exemplaire_filepath_to_list(filepath) for filepath in filepath_list if os.path.isfile(filepath)
    ]
    values_by_size: Dict[int, List[float]] = {}
    for exemplaire in exemplaires_list:
        size = len(exemplaire)
        print(f"computing exemplaire of size {size}")
        point = values_by_size.get(size)
        if point:
            point.append(execute_brute_force(exemplaire))
        else:
            values_by_size[size] = [execute_brute_force(exemplaire)]
    graph_points = {key: np.mean(value) for key, value in values_by_size.items()}
    print(graph_points)

    puissanceGraph(np.log2(list(graph_points.keys())), np.log2(list(graph_points.values())), "Force brute")

    ratioBF1 = genRatioExpArray(list(graph_points.values()), list(graph_points.keys()), lambda x: x ** 1.9)
    ratioBF2 = genRatioExpArray(list(graph_points.values()), list(graph_points.keys()), lambda x: x ** 2)
    ratioBF3 = genRatioExpArray(list(graph_points.values()), list(graph_points.keys()), lambda x: x ** 2.1)
    rapportGraph(list(graph_points.keys()), ratioBF1, ' - limite gauche (x^1.9)')
    rapportGraph(list(graph_points.keys()), ratioBF2, ' - centre (x^2.0)')
    rapportGraph(list(graph_points.keys()), ratioBF3, ' - limite droite (x^2.1)')


def profile_all_for_given_size(flag, seuil):
    files = get_filepath_list_from_directory_path()
    if flag:
        bfMean = get_mean_time_from_brute_force(files)
    else:
        bfMean = 1
    DpRMean = dprAlgoExecuter(files, 1)
    DpRMeanSeuil = dprAlgoExecuter(files, seuil)
    return bfMean, DpRMean, DpRMeanSeuil


def get_filepath_list_from_directory_path():
    path = './profiling/data'
    files = None
    try:
        files = glob.glob(path + '/*')
    except:
        print('Path', path, 'not found')
    return files


def dprAlgoExecuter(files, seuil):
    DpRData = []
    for f in files:
        x, y = utils.text_parser.get_sorted_xs_and_ys_from_filepath(f)
        DpRTime = execute_DpR(x, y, seuil)
        print('DpR ' + str(seuil) + ' (time): ', DpRTime)
        DpRData.append(DpRTime)
    return np.mean(DpRData)


def get_mean_time_from_brute_force(files):
    bfData = []
    for f in files:
        if os.path.isdir(f):
            continue
        points = utils.text_parser.parse_exemplaire_filepath_to_list(f)
        bfTime = execute_brute_force(points)
        print('BF(time)     : ', bfTime)
        bfData.append(bfTime)
    return np.mean(bfData)


def writeGraph(dataBF, dataDpR, dataDpRSeuil, dataNb, seuil):
    graphGenerator(dataBF, dataDpR, dataDpRSeuil, dataNb, seuil)


def askBF():
    choices = {'y', 'Y', 'n', 'N'}
    choice = None
    while choice not in choices:
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
