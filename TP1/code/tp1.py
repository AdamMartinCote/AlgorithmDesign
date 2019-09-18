#!/usr/bin/env python3

import argparse

# from TP1.code.algorithms.bruteforce import brute_force
from algorithms.bruteforce import brute_force

# if __name__ == "__main__":
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--algorithme",
                    choices=['brute', 'seuil'],
                    help="algorithme utilisé")
parser.add_argument("-e", "--path_vers_exemplaire",
                    help="path to exemplaire")
parser.add_argument("-p", "--show_p", action='store_true',
                    help="affiche la plus petite distance entre deux points, sans texte superflu")
parser.add_argument("-t", "--show_t", action='store_true',
                    help="affiche le temps d’exécution en ms, sans unité ni texte superflu")
args = parser.parse_args()

if args.algorithme == 'brute':
    val = brute_force([(1, 2), (4, 4)])
    print(val)
elif args.algorithme == 'seuil':
    pass
