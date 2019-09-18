#!/usr/bin/env python3

import argparse

if __name__ == "__main__":
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

    print(args)
