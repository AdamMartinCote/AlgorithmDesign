#!/usr/bin/env python3

import argparse

default_path = './exemplaires/10-6.txt'

parser = argparse.ArgumentParser()

parser.add_argument("-e", "--path_vers_exemplaire",
                    help="specifier le chemin d'un exemplaire (fichier ou répertoire)")

args = parser.parse_args()

if args.path_vers_exemplaire is None:
    parser.print_usage()
    exit(-1)

print("foo")
