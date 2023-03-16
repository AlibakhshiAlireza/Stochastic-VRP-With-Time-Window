from itertools import combinations
from phase import *
from phasetypes import *
from reader import *
import random

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






def NurseCons(testcase,nurses):
    zero_indexes = zeroindexes(testcase)
    if len(zero_indexes) > nurses:
        a = False
    else:
        a = True
    return a

def feasibility(TestCase, TW, nurses):
    f = zeroindexes(TestCase)
    f.append(len(TestCase) - 1)
    probs=[]
    prob = []
    start = 0
    p = 1
    print(f)
    for i in f:
        temp = []
        for j in TestCase[start:i]:
            if j == 0:
                cd = TravelTimeDist
                nxtstp = TestCase[start:i][TestCase[start:i].index(j) + 1]
                temp.append(cd.LessThan(TW[nxtstp][1]))
            else:
                cd = phaseconvo(cd,ServiceTimeDist).Dist()
                cd = phaseconvo(cd,TravelTimeDist).Dist()
                nxtstp = TestCase[TestCase.index(j) + 1]
                temp.append(cd.LessThan(TW[nxtstp][1]))
        start = i
        p = np.prod(temp)
        probs.append(p)
        prob.append(temp)
#Depot Returnes
    for i in prob:
        if i[-1] < 0.95:
            dfeas = False
        else:
            dfeas = True
#every cus
    for i in prob:
        if any(x < 0.95 for x in i[:-1]):
            cfeas = False
            break
        else:
            cfeas = True
#complete route
    if np.prod(probs) < 0.95:
        pfeas = False
    else:
        pfeas = True
    ncon = NurseCons(TestCase,nurses)
    feaslist = [dfeas,cfeas,pfeas,ncon]
    print("List : ",prob)
    print("Prob : ",probs)
    print("p :",p)
    print(feaslist)
    if any(x == False for x in feaslist):
        return False
    else:
        return True

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



nurses,patients,TW = reader("A7")
print(patients)
lst = list(range(1, int(patients)+1))
random.shuffle(lst)
lst = interleave_zeros(lst)
zero_indexes = zeroindexes(lst)
lcombinations = list(combinations(zero_indexes, 9))
o = list(lcombinations[0])
my_list = [lst[y] for y in range(len(lst)) if y not in o]
print(my_list)
g = feasibility(my_list,TW,nurses)
print(g)