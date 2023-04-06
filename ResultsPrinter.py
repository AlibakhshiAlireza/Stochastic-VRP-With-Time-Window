import numpy as np
import sys
sys.path.append('butools2/Python')
sys.path.append('MPMAVRPMain/butools2/Python')
import random
import matplotlib.pyplot as plt
from initpop import *
from reader import *
from utils import *
from phasetypes import *
from butools.ph import *
from butools.fitting import *
from matplotlib import rc
ins = ['A1','A2','A3','A4','A5','A6','A7','B1','B2','B3','B4','B5','B6','B7','C1','C2','C3','C4','C5','C6','C7']
for i in ins:
    with open('PSOSOL/'+i+'.txt', 'r') as f:
        content = f.readlines()
        a = content[3].split('[')[-1].split(']')[0].split(',')
        a = [int(i) for i in a]
        b = Split(i,permutation=a)
        print(i,',',len(b[0][0]))
        print(i,',',b[2])
