import time
from TP1.code.algorithms.utils import MAX_DIST, distance


def brute_force(points) -> float:
    """ Si le nombre de points est suffisamment petit, on préfère utiliser cet algorithme.
    """
    dist_min = MAX_DIST
    for pos, pt1 in enumerate(points):
        for pt2 in points[(pos + 1):]:
            tmp_dist = distance(pt1, pt2)
            dist_min = min(tmp_dist, dist_min)
    return dist_min


def execute_brute_force(points) -> float:
    start = time.time()
    min_brute_force = brute_force(points)
    end = time.time()
    # print("BF: ", min_brute_force)
    return end - start


if __name__ == "__main__":
    """ dummy """
    print(brute_force([(1, 2), (56, 1), (3, 3), (5, 56)]))
