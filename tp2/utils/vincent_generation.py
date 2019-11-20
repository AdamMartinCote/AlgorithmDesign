
import glob
import os
import numpy as np
from src.roll import Roll

def meansGeneration(algo):
    path = './exemplaires'
    files = None
    try:
        files = sorted(glob.glob(path + '/*'))
    except:
        print('Path', path, 'not found')
        
    meanTimes = []
    meanValues = []
    rollSizes = []
    times = []
    values = []
    i=0
    for f in files:
        i+=1
        if(not(i%10) and not i==0):
            roll = Roll(f)
            t,p = algo(roll)
            times.append(t)
            values.append(p)
            meanValues.append(np.mean(values))
            meanTimes.append(np.mean(times))
            rollSizes.append(shrinkFileName(f))
            print('MEAN TIME:',np.mean(times))
            print('MEAN TIME:',np.mean(values))
            times = []
            values = []
            i=0
            print('----------')
        else:
            roll = Roll(f)
            t,p=algo(roll)
            times.append(t)
            values.append(p)
    print(np.sort(meanTimes))
    print(np.sort(meanValues)) 
    return np.sort(meanTimes), np.sort(rollSizes),np.sort(meanValues)

def singleGeneration(algo):
    path = './exemplaires'
    files = None
    try:
        files = sorted(glob.glob(path + '/*'))
    except:
        print('Path', path, 'not found')
        
    rollSizes = []
    times = []
    values = []
    for fileIndex in range(0,len(files),10):
        rollSizes.append(shrinkFileName(files[fileIndex]))
        roll = Roll(files[fileIndex])
        t, p = algo(roll)
        times.append(t)
        values.append(p)

    return np.sort(times), np.sort(rollSizes), np.sort(values)

def shrinkFileName(fileName):
    dataSize = '' 
    for character in fileName:
        if character == '-':
            return int(dataSize)
        if character.isnumeric():
            dataSize+=character