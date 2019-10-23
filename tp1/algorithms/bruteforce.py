import time
from typing import List

from .common import MAX_DIST, distance


def brute_force(points: List[List[int]]) -> float:
    """ Si le nombre de points est suffisamment petit, on préfère utiliser cet algorithme.
    """
    dist_min = MAX_DIST
    for pos, pt1 in enumerate(points):
        for pt2 in points[(pos + 1):]:
            tmp_dist = distance(pt1, pt2)
            dist_min = min(tmp_dist, dist_min)
    return dist_min


def execute_brute_force(points) -> float:
    if 'min_dist' not in execute_brute_force.__dict__:
        execute_brute_force.min_dist = 999999
    start = time.time()
    min_brute_force = brute_force(points)
    if execute_brute_force.min_dist > min_brute_force:
        execute_brute_force.min_dist = min_brute_force
    end = time.time()
    return end - start
