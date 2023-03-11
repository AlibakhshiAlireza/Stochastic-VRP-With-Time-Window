import numpy as np
import pandas as pd
from itertools import combinations
permutation = [2,4,1,5,3]
TW = {2:[25,40],4:[40,90],1:[60,95],5:[30,60],3:[35,85],0:[0,160]}
tt = np.array([[0,20,25,25,30,15],[20,0,0,0,0,20],[25,0,0,0,20,0],[25,0,0,0,0,0],[30,20,0,0,0,0],[15,0,0,20,0,0]])
servicecost = [0,20,20,20,20,20]
routes = {}
for i in permutation:
  time = 0
  cost = 0
  temp = []
  print(permutation.index(i))
  time = time + tt[0,i] + servicecost[i]
  cost = tt[0,i] + servicecost[i] 
  routes[i] = {}
  routes[i][i]= cost + tt[0,i]
  for j in permutation[permutation.index(i) + 1:]:
    #print(i,j,TW[j][1],time,time + tt[permutation.index(j) - 1,j],cost)
    if time + tt[0,j] + servicecost[j] + tt[permutation[permutation.index(j)-1],j] <160 and time + tt[permutation[permutation.index(j) - 1],j] < TW[j][1] :
      time = time + tt[permutation[permutation.index(j) - 1],j] + servicecost[j]
      cost = cost + tt[permutation[permutation.index(j) - 1],j] + servicecost[j]
      routes[i][j] = cost + tt[0,j]
    else:
      #routes[i][j] = cost + tt[0,j]
      break


#split method by prince
permutation = [2,4,1,5,3]
completeroute = [2,0,4,0,1,0,5,0,3]
zero_indexes = [i for i, x in enumerate(completeroute) if x == 0]
finsteps = len(permutation)
steps = 1
lenstep = len(permutation) - 1
listofroutes = []
listofroutes.append(completeroute)
temp = completeroute.copy()
while steps < len(permutation):
    lcombinations = list(combinations(zero_indexes, steps))
    for i in lcombinations:
        temp = completeroute.copy()
        o = list(i)
        #delete o as index from temp
        my_list = [temp[y] for y in range(len(temp)) if y not in i]
        listofroutes.append(my_list)
    steps = steps + 1
print(len(listofroutes))


        
      