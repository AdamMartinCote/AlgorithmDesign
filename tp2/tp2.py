#!/usr/bin/env python3
import argparse

from src.algorithms.backtracking import Backtracking
from src.algorithms.dynamic import Dynamic
from src.algorithms.greedy import Greedy
from src.roll import Roll
from utils.vincent_generation import meansGeneration,singleGeneration
from utils.graph_generator import writeGraph
import numpy as np
default_path = './exemplaires/10-6.txt'

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--algorithme",
                    choices=['glouton', 'progdyn', 'backtrack'],
                    help="algorithme utilisé")
parser.add_argument("-e", "--path_vers_exemplaire",
                    help="specifier le chemin d'un exemplaire (fichier ou répertoire)")
parser.add_argument("-p", "--show_p", action='store_true',
                    help="affiche le prix total des coupes choisies, sans unité ni texte superflu")
parser.add_argument("-t", "--show_t", action='store_true',
                    help="affiche le temps d'exécution en ms, sans unité ni texte superflu")
parser.add_argument("-c", "--solution", action='store_true',
                    help="affiche la solution (coupes i choisies) sur une ligne, "
                         "avec chaque coupe séparée par un espace")
parser.add_argument("-v", "--dataGenerator",action='store_true',
                    help="pour une génération de graphique comprise")
args = parser.parse_args()

algo = None
options = {'display_time': args.show_t,
           'display_price': args.show_p,
           'display_solution': args.solution,
           'display_graphs': args.dataGenerator}

if args.algorithme == 'glouton':
    times = [2.62975693e-05 ,9.31978226e-05, 3.78465652e-04 ,9.61494446e-04,4.71427441e-03 ,1.02265358e-02, 2.43540764e-02, 2.80307055e-02,3.78087759e-02]
    algo = Greedy(**options)

elif args.algorithme == 'progdyn':
    times = [8.55684280e-05 ,1.26273632e-03, 2.05910206e-02, 1.33548379e-01,2.21826499e+00, 1.56254653e+01, 6.06585704e+01, 1.37532989e+02,2.43371290e+02]
    algo = Dynamic(**options)
elif args.algorithme == 'backtrack':
    times = [0.008165836334228516,600000,600000,600000,600000,600000,600000,600000,600000]
    algo = Backtracking(**options)
else:
    parser.print_usage()

if args.dataGenerator:
    rollSizes = [10, 100, 400, 1000, 4000, 10000, 20000, 30000, 40000]
    # meanTimes,rollSizes,meanValues = meansGeneration(algo)
    # times, rollSizes,values = singleGeneration(algo)
    writeGraph(times,rollSizes)
else:  
    path = args.path_vers_exemplaire or default_path
    roll = Roll(path)
    algo(roll)
