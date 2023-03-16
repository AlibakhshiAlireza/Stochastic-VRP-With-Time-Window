from itertools import combinations
from phase import *
from phasetypes import *

def interleave_zeros(lst):
    new_list = []
    for num in lst:
        new_list.extend([0, num])
    new_list.append(0)
    return new_list

def zeroindexes(x):
    zero_indexes = [i for i, x in enumerate(x) if x == 0]
    zero_indexes.pop(0)
    zero_indexes.pop(-1)
    return zero_indexes






def Splitfunc(completeroute,zero_indexes):
    """
    x = permutation  list
    y = interleave_zeros(x) list
    """
    steps = 1
    while steps <= len(zero_indexes) :
        lcombinations = list(combinations(zero_indexes, steps))
        for i in lcombinations:
            temp = completeroute.copy()
            o = list(i)
        #delete o as index from temp
            my_list = [temp[y] for y in range(len(temp)) if y not in i]
            ################ here will be a feasibility check and cost calculation
        steps = steps + 1

def NurseCons(testcase,nurses):
    zero_indexes = zeroindexes(testcase)
    if len(zero_indexes) > nurses:
        a = False
    else:
        a = True
    return a

TestCase = [0,1,2,0,3,0,4,5,0]
TW = {0: [0, 360000], 1: [2000, 4000], 2: [3000, 6000], 3: [50000, 70000], 4: [4000, 8000], 5: [1000, 100000]}
f = zeroindexes(TestCase)
f.append(len(TestCase))
probs = []
start = 0
for i in f:
    temp = []
    p = 0
    cd = None
    for j in TestCase[start:i]:
        if j == 0:
            cd = TravelTimeDist
            nxtstp = TestCase[TestCase.index(j) + 1]
            temp.append(cd.LessThan(TW[nxtstp][1]))
            state = 1
        else:
            cd = phaseconvo(cd,ServiceTimeDist).Dist()
            cd = phaseconvo(cd,TravelTimeDist).Dist()
            nxtstp = TestCase[TestCase.index(j) + 1]
            temp.append(cd.LessThan(TW[nxtstp][1]))
    start = i
    print(temp)
