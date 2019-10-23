import argparse

import profiling.profile_script as profiler
from utils.automaticGen import gen

display_time = False

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--algorithme",
                    choices=['brute', 'seuil'],
                    help="algorithme utilisé")
parser.add_argument("-e", "--path_vers_exemplaire",
                    help="specifier le chemin d'un exemplaire (fichier ou répertoire)")
parser.add_argument("-p", "--show_p", action='store_true',
                    help="affiche la plus petite distance entre deux points, sans texte superflu")
parser.add_argument("-t", "--show_t", action='store_true',
                    help="affiche le temps d’exécution en ms, sans unité ni texte superflu")
parser.add_argument("-g", "--generate",
                    help="génère un exemplaire de taille N")
parser.add_argument("-r", "--repetitions",
                    help="nombre d'exemplaires à générer")
parser.add_argument("-s", "--seuil",
                    help="seuil à utiliser (valeur par défaut = 1)")
args = parser.parse_args()

options = {'display_time': args.show_t,
           'display_distance': args.show_p,
           'seuil': int(args.seuil) or 1}

if args.algorithme == 'brute':
    if args.path_vers_exemplaire:
        profiler.profile_brute_force(args.path_vers_exemplaire, **options)
    else:
        profiler.profile_brute_force(**options)
elif args.algorithme == 'seuil':
    if args.path_vers_exemplaire:
        profiler.profile_seuil(exemplaire_path=args.path_vers_exemplaire, **options)
    else:
        profiler.profile_seuil(**options)


elif args.generate:
    gen(int(args.generate), int(args.repetitions) or 3)


else:
    parser.usage()
