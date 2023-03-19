from itertools import combinations
from phase import *
from phasetypes import *
from reader import *
import random
from tqdm import tqdm
import itertools

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





def Split(instance,permutation):
    nurses,patients,TW = reader(instance)
    Costmat = matcord(rcord(instance))
    p = {}
    pred = {}
    rt = permutation
    a = rt.copy()
    for i in a:
        pred[i] = []
    p[0] = 0
    for i in a:
        p[i] = np.inf

    dummy = a.copy()
    dummy.insert(0,0)
    dummy.pop(-1)
    a.insert(0,0)
    for idx,t in enumerate(dummy):
        i = idx + 1
        time = 0
        Dist = None
        while i <= patients and TravelTimeDist.LessThan((TW[0][1] - time)) >= 0.95 and phaseconvo(Dist,TravelTimeDist).Dist().LessThan(TW[a[i]][1]) >= 0.95:
            time += TravelTimeDist.sample() + ServiceTimeDist.sample()
            Dist = phaseconvo(Dist,TravelTimeDist).Dist()
            Dist = phaseconvo(Dist,ServiceTimeDist).Dist()
            if i == t + 1:
                cost = Costmat[0][a[i]]
            else:
                cost = cost + Costmat[a[i-1]][a[i]]
                lop = TW[a[i]][1] - time
                if lop < 0:
                    cost = cost + 2*Costmat[0][a[i]]
                else:
                    cost = cost + TravelTimeDist.GreaterThan(lop)*2*Costmat[0][a[i]]
            if p[a[idx]] + cost + Costmat[a[i]][0] < p[a[i]]:
                p[a[i]] = p[a[idx]] + cost + Costmat[a[i]][0]
                pred[a[i]].append(a[idx])
            i += 1



    E = [dict(zip(pred.keys(), a)) for a in itertools.product(*pred.values())]

    z = []
    for i in E:
        s = []
        j = patients
        while j != 0:
            trip = []
            for k in a[a.index(i[a[j]]) + 1:j + 1]:
                trip.append(k)
            s.insert(0,trip)
            j = a.index(i[a[j]])
        z.append(s)
    temp = []
    for i in z:
        if i in temp:
            pass
        else:
            temp.append(i)
    return temp


