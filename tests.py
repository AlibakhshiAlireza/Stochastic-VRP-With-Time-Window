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
steps = 9
shuffle(a)
a = interleave_zeros(a)
zero_indexes = zeroindexes(a)
lcombinations = list(combinations(zero_indexes, steps))
my_list = [a[y] for y in range(len(a)) if y not in lcombinations[0]]
print(feasibility(my_list,TW,nurses))