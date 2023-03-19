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
import itertools
starttimer = time.time()
nurses,patients,TW = reader('A7')
Costmat = matcord(rcord('A7'))
#OBJ = M + \Sigma cr + \resourcecost
a = list(range(1,patients+1))
p = {}
pred = {}
for i in range(1,patients+1):
    pred[i] = []
p[0] = 0
for i in range(1,patients+1):
    p[i] = np.inf
for t in range(0,patients):
    i = t + 1
    time = 0
    Dist = None
    while i <= patients and TravelTimeDist.LessThan((TW[0][1] - time)) >= 0.95 and phaseconvo(Dist,TravelTimeDist).Dist().LessThan(TW[i][1]) >= 0.95:
        time += TravelTimeDist.sample() + ServiceTimeDist.sample()
        Dist = phaseconvo(Dist,TravelTimeDist).Dist()
        Dist = phaseconvo(Dist,ServiceTimeDist).Dist()
        if i == t + 1:
            cost = Costmat[0][i]
        else:
            cost = cost + Costmat[i-1][i]
        if p[t] + cost + Costmat[i][0] < p[i]:
            p[i] = p[t] + cost + Costmat[i][0]
            pred[i].append(t)
        i += 1

print(p)
print(pred)
s = []
j = patients
while j != 0:
    trip = []
    for k in range(int(pred[j][0]) + 1,j + 1):
        trip.append(k)
    s.insert(0,trip)
    j = int(pred[j][0])

E = [dict(zip(pred.keys(), a)) for a in itertools.product(*pred.values())]
print(len(E))
print(E[1])

s = []
j = patients
while j != 0:
    trip = []
    for k in range(int(E[0][j]) + 1,j + 1):
        trip.append(k)
    s.insert(0,trip)
    j = int(E[0][j])
print(s)