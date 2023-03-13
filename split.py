import numpy as np
import pandas as pd
from itertools import combinations
from utils import *
TW = {2:[25,40],4:[40,90],1:[60,95],5:[30,60],3:[35,85],0:[0,160]}
tt = np.array([[0,20,25,25,30,15],[20,0,0,0,0,20],[25,0,0,0,20,0],[25,0,0,0,0,0],[30,20,0,0,0,0],[15,0,0,20,0,0]])
servicecost = [0,20,20,20,20,20]


#split method by prince
permutation = [2,4,1,5,3]
completeroute = interleave_zeros(permutation)
print(len(permutation),completeroute,len(completeroute))
zero_indexes = [i for i, x in enumerate(completeroute) if x == 0]
zero_indexes.pop(0)
zero_indexes.pop(-1)
finsteps = len(permutation)
steps = 1
lenstep = len(permutation) - 1
listofroutes = []
listofroutes.append(completeroute)
temp = completeroute.copy()
while steps < len(zero_indexes) + 1:
    lcombinations = list(combinations(zero_indexes, steps))
    for i in lcombinations:
        temp = completeroute.copy()
        o = list(i)
        #delete o as index from temp
        my_list = [temp[y] for y in range(len(temp)) if y not in i]
        listofroutes.append(my_list)
    steps = steps + 1
print(listofroutes[2])


        
      