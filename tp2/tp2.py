import argparse

#from src.algorithms.dynamic import Dynamic
from src.algorithms.greedy import Greedy
from src.roll import Roll

display_time = False

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

options = {'display_time': args.show_t,
           'display_distance': args.show_p,
           'display_solution': args.solution}

if args.algorithme == 'glouton':
    algo = Greedy()
    path = './exemplaires/10-1.txt'
    roll = Roll(path)
    algo.optimize_exemplaire(roll, **options)

elif args.algorithme == 'progdyn':
    raise NotImplemented
elif args.algorithme == 'backtrack':
    raise NotImplemented

else:
    parser.print_usage()
