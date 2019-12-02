#!/usr/bin/env python3

import argparse

from tp3.src.exemplaire import Exemplaire

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--path_vers_exemplaire",
                    help="specifier le chemin d'un exemplaire (fichier ou répertoire)")

args = parser.parse_args()
filepath = args.path_vers_exemplaire

if filepath is None:
    parser.print_usage()
    exit(-1)

exemplaire = Exemplaire(filepath)

