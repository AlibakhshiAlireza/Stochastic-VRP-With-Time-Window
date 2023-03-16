import os
import sys

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

nurses,patirnts,TW = reader("A7")

print(patirnts)


