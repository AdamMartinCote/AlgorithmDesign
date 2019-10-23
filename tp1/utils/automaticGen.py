import random


def gen(nbData, nbFiles):
    for i in range(nbFiles):
        fn = 'profiling/data/' + str(nbData) + '-' + str(i) + '.txt'
        c = 1000000
        points = [[random.randint(0, c), random.randint(0, c)] for _ in range(nbData)]
        with open(fn, 'w') as f:
            f.write(str(nbData) + '\n')
            for i in range(nbData):
                f.write(str(points[i][0]) + ' ' + str(points[i][1]) + '\n')
        f.close()
