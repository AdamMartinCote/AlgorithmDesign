import random
import os
import glob


def gen(nbData, nbFiles):
    path = './code/profiling/data'
    #try:
    #    os.mkdir(path)
    #except:
    #    #print('Removing previous data...\n')
    #    files = glob.glob(path + '/*')
    #    for f in files:
    #        os.remove(f)

    for i in range(nbFiles):
        fn = 'code/profiling/data/' + str(nbData) + '-' + str(i) + '.txt'
        c = 1000000
        points = [[random.randint(0, c), random.randint(0, c)] for _ in range(nbData)]
        with open(fn, 'w') as f:
            f.write(str(nbData) + '\n')
            for i in range(nbData):
                f.write(str(points[i][0]) + ' ' + str(points[i][1]) + '\n')
        f.close()
