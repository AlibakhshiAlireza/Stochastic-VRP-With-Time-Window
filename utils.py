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


def costmatrix(cord):
    return 0



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
    if np.prod(probs) < 0.90:
        pfeas = False
    else:
        pfeas = True
    ncon = NurseCons(TestCase,nurses)
    feaslist = [dfeas,cfeas,pfeas,ncon]
    #print(feaslist)
    if any(x == False for x in feaslist):
        return False
    else:
        return True


def CostFunc(TW, Costmat, my_list):
    routelist = []
    temp = zeroindexes(my_list)
    temp.append(len(my_list) - 1)
    start = 0
    for i in temp:
        routelist.append(my_list[start:i+1])
        start = i
    TotalCost = []
    TotalResourceCost = []
    Time = []
    for i in routelist:
        time = 0
        cost = 0
        resourcecost = 0
        for index,j in enumerate(i):
            if index == 0:
                cost += Costmat[0,i[index+1]]
                lop = TW[i[index+1]][1] - time
                if lop <= 0:
                    resourcecost += 2*Costmat[0][i[index+1]]
                else:
                    resourcecost += TravelTimeDist.GreaterThan(lop)*2*Costmat[0][i[index+1]]
                time += TravelTimeDist.sample()
                if time < TW[i[index+1]][0]:
                    time = TW[i[index+1]][0]
                else:
                    pass
                time += ServiceTimeDist.sample()
            elif index == len(i)-1:
                pass
            elif index == len(i)-2:
                cost += Costmat[0,j]
                time += TravelTimeDist.sample()
            else:
                cost += Costmat[j,i[index+1]]
                lop = TW[i[index+1]][1] - time
                if lop <= 0:
                    resourcecost += 2*Costmat[0][i[index+1]]
                else:
                    resourcecost += TravelTimeDist.GreaterThan(lop)*2*Costmat[0][i[index+1]]
                time += TravelTimeDist.sample()
                if time < TW[i[index+1]][0]:
                    time = TW[i[index+1]][0]
                else:
                    pass
                time += ServiceTimeDist.sample()
        TotalCost.append(cost)
        TotalResourceCost.append(resourcecost)
        Time.append(time)
    return sum(TotalCost),sum(TotalResourceCost)

def Splitfunc(completeroute,zero_indexes,TW,nurses,costmat):
    """
    x = permutation  list
    y = interleave_zeros(x) list
    incomplete
    """
    steps = 1
    Vi = np.inf
    while steps <= len(zero_indexes) :
        lcombinations = list(combinations(zero_indexes, steps))
        for i in lcombinations:
            temp = completeroute.copy()
            o = list(i)
            #delete o as index from temp
            my_list = [temp[y] for y in range(len(temp)) if y not in i]
            ################ here will be a feasibility check and cost calculation
            if feasibility(my_list, TW, nurses) == True:
                tc,rc = CostFunc(TW, costmat, my_list)
                if rc + tc < Vi:
                    Vi = tc + rc
                    best = my_list
                    print(Vi)
                    print(best)
                else:
                    pass
            else:
                pass
        steps = steps + 1
    return best,Vi


