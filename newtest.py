from phase import *
from phasetypes import *
from reader import *
from random import shuffle
from utils import *
import sys
sys.path.append('butools2/Python')
sys.path.append('MPMAVRPMain/butools2/Python')
from butools.ph import *
from butools.fitting import *
import time
import math
nurses,patients,TW = reader('C7')
Costmat = matcord(rcord('C7'))
starttimer = time.time()
permutation = list(range(1,patients+1))
shuffle(permutation)
splits = Split('C7',permutation=permutation)
print(splits[2])
a = Feasibility(nurses=nurses,TW=TW, splits=splits)
"""a = Feasibility(nurses=nurses,TW=TW, splits=splits)

testziz = a[0]
excost = 0
resourcecost = 0
trc = 0
veichles = len(testziz)
for i in testziz:
    time = 0
    for idx,j in enumerate(i):
        if idx == 0:
            trc += Costmat[0][i[idx + 1]]
            if TW[i[idx + 1]][1] - time >= 0:
                resourcecost += (TravelTimeDist.GreaterThan((TW[i[idx + 1]][1] - time))*2*(Costmat[0][i[idx + 1]]))
            else:
                resourcecost += (TravelTimeDist.GreaterThan(0)*2*(Costmat[0][i[idx + 1]]))
            time = TravelTimeDist.sample()
            if time >= TW[i[idx + 1]][1]:
                time = time
            else:
                time = TW[i[idx + 1]][1]
        elif idx == (len(i) - 2):
            trc += Costmat[i[idx]][0]
            time += TravelTimeDist.sample() + ServiceTimeDist.sample()
        elif idx == (len(i) - 1):
            pass
        else:
            trc += Costmat[i[idx]][i[idx + 1]]
            time += ServiceTimeDist.sample()
            if TW[i[idx + 1]][1] - time >= 0:
                resourcecost += (TravelTimeDist.GreaterThan((TW[i[idx + 1]][1] - time))*2*(Costmat[i[idx]][0]))
            else:
                resourcecost += (TravelTimeDist.GreaterThan(0)*2*(Costmat[i[idx]][0]))
            time += TravelTimeDist.sample()
            if time >= TW[i[idx + 1]][1]:
                time = time
            else:
                time = TW[i[idx + 1]][1]

print(trc)
print(resourcecost)
print(veichles)
print(time)"""