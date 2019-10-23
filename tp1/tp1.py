import argparse

import profiling.profile_script as profiler
from algorithms.seuil import seuil
from utils.automaticGen import gen

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--algorithme",
                    #required=True,
                    choices=['brute', 'seuil', 'profile'],
                    help="algorithme utilisé")
parser.add_argument("-e", "--path_vers_exemplaire",
                    help="specifier le chemin d'un exemplaire")
parser.add_argument("-p", "--show_p", action='store_true',
                    help="affiche la plus petite distance entre deux points, sans texte superflu")
parser.add_argument("-t", "--show_t", action='store_true',
                    help="affiche le temps d’exécution en ms, sans unité ni texte superflu")
parser.add_argument("-g", "--generate",
                    help="genere un exemplaire de taille N")
parser.add_argument("-r", "--repetitions")
args = parser.parse_args()

if args.algorithme == 'brute':
    raise NotImplemented
elif args.algorithme == 'seuil':
    val = seuil([[1, 2], [3, 4]], [[2, 3], [4, 5]], 1)
    print(val)

elif args.algorithme == 'profile':
    #profiler.collectResults()
    profiler.profile_brute_force()

elif args.generate:
    gen(int(args.generate), args.repetitions or 3)

