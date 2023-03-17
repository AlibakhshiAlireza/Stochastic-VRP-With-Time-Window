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

nurses,patients,TW = reader('A7')
Costmat = matcord(rcord('A7'))
#OBJ = M + \Sigma cr + \resourcecost
a = list(range(1,patients+1))
steps = 4
shuffle(a)
a = interleave_zeros(a)
zero_indexes = zeroindexes(a)
lcombinations = list(combinations(zero_indexes, steps))
my_list = [a[y] for y in range(len(a)) if y not in lcombinations[3]]
edgecost = 0 
resourcecost = 0
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
            resourcecost = (TravelTimeDist.GreaterThan(TW[i[index+1]][1])*2*(Costmat[0][i[index+1]]))
            time += TravelTimeDist.sample() + ServiceTimeDist.sample()
        elif index == len(i)-1:
            pass
        elif index == len(i)-2:
            cost += Costmat[0,j]
            time += TravelTimeDist.sample()
        else:
            cost += Costmat[j,i[index+1]]
            resourcecost += (TravelTimeDist.GreaterThan(TW[i[index+1]][1] - time)*2*(Costmat[j][i[index+1]]))
            time += TravelTimeDist.sample() + ServiceTimeDist.sample()
    TotalCost.append(cost)
    TotalResourceCost.append(resourcecost)
    Time.append(time)
print(Costmat)
print(TotalCost)
print(routelist)
print(TotalResourceCost)
print(feasibility(my_list,TW,6))
