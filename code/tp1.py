#!/usr/bin/env python3

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--algorithm",
                        help="algorithm to use")
    parser.add_argument("-e", "--ex_path",
                        help="")
    parser.add_argument("-p", "--show_p", action='store_true',
                        help="")
    parser.add_argument("-t", "--show_t", action='store_true',
                        help="")
    args = parser.parse_args()

    print(args)
