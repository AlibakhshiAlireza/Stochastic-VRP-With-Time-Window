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
nurses,patients,TW = reader('A7')
starttimer = time.time()
temp = Split('A7',[3,4,5,8,7,9,2,1,6,10])
Dist = None
P = []
for i in temp[1]:
    i.append(0)
    i.insert(0,0)
    p = []
    for index,j in enumerate(i):
        if j == 0:
            Dist = TravelTimeDist
            x1 = TravelTimeDist.LessThan(TW[0][1])
            p.append(x1)
        elif index == (len(i) - 2):
            Dist = phaseconvo(Dist,TravelTimeDist).Dist()
            Dist = phaseconvo(Dist,ServiceTimeDist).Dist()
            x2 = Dist.LessThan(TW[0][1])
            p.append(x2)
        elif index == (len(i) - 1):
            pass
        else:
            Dist = phaseconvo(Dist,TravelTimeDist).Dist()
            Dist = phaseconvo(Dist,ServiceTimeDist).Dist()
            x3 = Dist.LessThan(TW[i[index+1]][1])
            p.append(x3)
    P.append(math.prod(p))

print(math.prod(P))
