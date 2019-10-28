import argparse

from src.algorithms.backtracking import Backtracking
from src.algorithms.dynamic import Dynamic
from src.algorithms.greedy import Greedy
from src.roll import Roll

display_time = False
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
args = parser.parse_args()

algo = None
options = {'display_time': args.show_t,
           'display_price': args.show_p,
           'display_solution': args.solution}

if args.algorithme == 'glouton':
    algo = Greedy(**options)

elif args.algorithme == 'progdyn':
    algo = Dynamic(**options)
elif args.algorithme == 'backtrack':
    algo = Backtracking(**options)
else:
    parser.print_usage()

path = args.path_vers_exemplaire or default_path
roll = Roll(path)
algo.optimize_exemplaire(roll)

