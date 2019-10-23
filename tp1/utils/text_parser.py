from typing import List

from utils.quick import quicksort


def parse_exemplaire_filepath_to_list(file_path) -> List[List[int]]:
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


def get_sorted_xs_and_ys_from_filepath(file_path) -> (List[int], List[int]):
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


