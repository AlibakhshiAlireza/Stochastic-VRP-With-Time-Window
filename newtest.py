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
"""nurses,patients,TW = reader('C7')
Costmat = matcord(rcord('C7'))
starttimer = time.time()
permutation = list(range(1,patients+1))
shuffle(permutation)
splits = Split('C7',permutation=permutation)
print(splits[2])
a = Feasibility(nurses=nurses,TW=TW, splits=splits)"""
MG = [1,2,3,4,5,6]
GP = [1,2,3,4,5,6]
list = [MG,GP]
with open('Soloutions\A7.txt','w') as f:
    for item in list:
        f.write(",".join(str(x) for x in item) + "\n")