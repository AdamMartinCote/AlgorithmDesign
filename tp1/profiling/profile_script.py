import glob
import os
from typing import List, Dict

import numpy as np

import utils.text_parser
from algorithms.bruteforce import execute_brute_force
from algorithms.seuil import execute_DpR
from utils.automaticGen import gen
from utils.graphGenerator import genRatioExpArray, rapportGraph
from utils.graphGenerator import puissanceGraph, constantesGraph
from utils.graphGenerator import writeGraph
from utils.text_parser import parse_exemplaire_filepath_to_list

start_at = 1
assay_number = 10
step = 1000
min_distance = 99999999

default_exemplaire_path = "./profiling/data"


def collectResults(exemplaire_path=default_exemplaire_path):
    dataBF = []
    dataDpR = []
    dataDpRSeuil = []
    dataNb = []
    bfFlag = askBF()
    seuil = askSeuil()
    for nbData in range(start_at * step, assay_number * step, step):
        gen(nbData, 3)  # arg1: Nombre de points , arg2: Nombre d'echantillons
        print('\nNumber of data: ', nbData, '\n')
        meanBf, meanDpR, meanDpRSeuil = profile_all_for_given_size(bfFlag, seuil, exemplaire_path)
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


def profile_brute_force(exemplaire_path=default_exemplaire_path, display_time=False, display_distance=False):
    exemplaires_list = get_exemplaire_list(exemplaire_path)
    values_by_size: Dict[int, List[float]] = {}
    for exemplaire in exemplaires_list:
        size = len(exemplaire)
        time_value = execute_brute_force(exemplaire)
        if display_time:
            print(str(size) + " ", end='')
            print(time_value)
        point = values_by_size.get(size)
        if point:
            point.append(time_value)
        else:
            values_by_size[size] = [time_value]
    graph_points = {key: np.mean(value) for key, value in values_by_size.items()}

    puissanceGraph(logx=np.log2(list(graph_points.keys())),
                   logy=np.log2(list(graph_points.values())),
                   name="Force brute")

    print_rapport_graph_with_limits(graph_points)

    print_constantes_graph(graph_points, algo_name="force brute")

    if display_distance:
        print(execute_brute_force.min_dist)


def print_constantes_graph(graph_points, algo_name):
    f = lambda x: x
    constantesGraph(list(map(f, graph_points.values())),
                    list(graph_points.keys()), name=f"algo_name")


def print_constantes_graph_iter(graph_points, algo_name):
    for i in np.arange(1, 3, 0.2):
        f = lambda x: x ** i
        constantesGraph(list(map(f, graph_points.values())),
                        list(graph_points.keys()), name=f"algo_name {i}")


def profile_seuil(seuil=1, exemplaire_path=default_exemplaire_path, display_time=False, display_distance=False):
    exemplaires_list = get_exemplaire_list(exemplaire_path)
    values_by_size: Dict[int, List[float]] = {}
    for exemplaire in exemplaires_list:
        size = len(exemplaire)
        time_value = execute_DpR(sorted(exemplaire, key=lambda x: x[0]),
                                 sorted(exemplaire, key=lambda x: x[1]),
                                 seuil)
        if display_time:
            print(time_value)
        point = values_by_size.get(size)
        if point:
            point.append(time_value)
        else:
            values_by_size[size] = [time_value]
    graph_points = {key: np.mean(value) for key, value in values_by_size.items()}

    puissanceGraph(logx=np.log2(list(graph_points.keys())),
                   logy=np.log2(list(graph_points.values())),
                   name=f"Recursif de seuil {seuil}")

    print_rapport_graph_with_limits(graph_points)

    print_constantes_graph(graph_points, algo_name=f"seuil {seuil}")

    if display_distance:
        print(execute_brute_force.min_dist)


def print_rapport_graph_with_limits(graph_points):
    exponent = 2.0
    delta = 0.1
    fs = [
        lambda x: x ** (exponent - delta),
        lambda x: x ** exponent,
        lambda x: x ** (exponent + delta),
    ]
    ratioBF1 = genRatioExpArray(list(graph_points.values()), list(graph_points.keys()), fs[0])
    ratioBF2 = genRatioExpArray(list(graph_points.values()), list(graph_points.keys()), fs[1])
    ratioBF3 = genRatioExpArray(list(graph_points.values()), list(graph_points.keys()), fs[2])
    rapportGraph(list(graph_points.keys()), ratioBF1, f' - limite gauche (x^{exponent - delta})')
    rapportGraph(list(graph_points.keys()), ratioBF2, f' - centre (x^{exponent})')
    rapportGraph(list(graph_points.keys()), ratioBF3, f' - limite droite (x^{exponent + delta})')


def get_exemplaire_list(exemplaire_path):
    filepath_list: List[str] = get_filepath_list_from_directory_path(exemplaire_path)
    exemplaires_list: List[(int, int,)] = [
        parse_exemplaire_filepath_to_list(filepath) for filepath in filepath_list if os.path.isfile(filepath)
    ]
    return exemplaires_list


def profile_all_for_given_size(flag, seuil, path):
    files = get_filepath_list_from_directory_path(path)
    if flag:
        bfMean = get_mean_time_from_brute_force(files)
    else:
        bfMean = 1
    DpRMean = dprAlgoExecuter(files, 1)
    DpRMeanSeuil = dprAlgoExecuter(files, seuil)
    return bfMean, DpRMean, DpRMeanSeuil


def get_filepath_list_from_directory_path(path):
    # path = './profiling/data'
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
