import os
import sys
import numpy as np

sys.path.append('MPMAVRPMain/Problem')
sys.path.append('Problem')
def reader(instance):
    TW = {}
    with open('Problem/'+instance+'.txt') as f:
        contents = f.readlines()
        nurses = int(contents[0].split('\n')[0])
        patients = int(contents[1].split('\n')[0])
        TW[0] = [int(contents[2].split(' ')[0]),int(contents[2].split(' ')[1][:-1])]
        for index,i in enumerate(contents[3:],start=1):
            TW[index] = [int(i.split(' ')[0]),int(i.split(' ')[1])]
    return nurses,patients,TW
def rcord(instance):
    cords =[]
    with open('Problem/'+instance+'C.txt') as f:
        contents = f.readlines()
        for idx,i in enumerate(contents):
            cords.append((float(i.split(' ')[0]),float(i.split(' ')[1])))
    return cords


def matcord(cord):
    mx = np.zeros((len(cord) - 1,len(cord)- 1))
    for i in range(len(cord) - 1):
        for j in range(len(cord) - 1):
            mx[i][j] = np.sqrt((cord[i][0]-cord[j][0])**2+(cord[i][1]-cord[j][1])**2)
    return mx


