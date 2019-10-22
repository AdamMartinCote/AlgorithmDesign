from utils.quick import quicksort
import numpy as np


def fileToArrayBruteMethod(file_path):
    f = open(file_path, "r")
    f.readline()  # Skip first line
    points = []
    try:
        for l in f:
            line = l.split()
            x = int(line[0])
            y = int(line[1])
            points.append([x, y])
    except:
        raise ValueError()
    f.close()
    return points


def fileToArraySeuilMethod(file_path):
    f = open(file_path, "r")
    f.readline()  # Skip first line
    xSortedPoints = []
    ySortedPoints = []
    points = []
    try:
        for l in f:
            line = l.split()
            x = int(line[0])
            y = int(line[1])
            points.append([x, y])
        xSortedPoints = quicksort(points, 0, len(points) - 1, 0)
        ySortedPoints = quicksort(points, 0, len(points) - 1, 1)
    except:
        raise ValueError()
    f.close()
    return xSortedPoints, ySortedPoints
