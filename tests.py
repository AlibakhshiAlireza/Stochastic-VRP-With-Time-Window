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
starttimer = time.time()
nurses,patients,TW = reader('C7')
Costmat = matcord(rcord('C7'))
#OBJ = M + \Sigma cr + \resourcecost
a = list(range(1,patients+1))
shuffle(a)
print("hi")
a = interleave_zeros(a)
zero_indexes = zeroindexes(a)
print("hi2")
print(Splitfunc(a,zero_indexes,TW,nurses,Costmat))
print(f'For Loop: {time.time() - starttimer} seconds')

