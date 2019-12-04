#!/usr/bin/env python3

import argparse

from tp3.exemplaire import Exemplaire
from tp3.solver import make_solution

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--path_vers_exemplaire",
                    help="specifier le chemin d'un exemplaire (fichier ou répertoire)")

args = parser.parse_args()
filepath = args.path_vers_exemplaire

if filepath is None:
    parser.print_usage()
    exit(-1)

exemplaire = Exemplaire(filepath)

solution = make_solution(exemplaire)

print(solution)

# with open('./foo', 'w') as f:
#     f.write(str(solution))
