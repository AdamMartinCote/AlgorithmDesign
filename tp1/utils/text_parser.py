import point 
import numpy as np

def txt_to_array(file_path):
    f = open(file_path,"r");f.readline() #Skip first line 
    points = []
    for l in f:
        line = l.split()
        x    = int(line[0])
        y    = int(line[1])
        pt = point.Point(x,y)
        points.append(pt)
    return points
# file_path = input("Your file path: ")
points = txt_to_array("./../code/tmp.txt")