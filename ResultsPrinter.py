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

with open('Soloutions/C7.txt', 'r') as f:
    content = f.readlines()

a = content[3].split('[')[-1].split(']')[0].split(',')
a = [int(i) for i in a]
b = Split('C7',permutation=a)
print(len(b[0][0]))
print(b[2])
try:
    chris = np.loadtxt('initsols/C7'+'CHRISTOFIDES.txt',dtype=int,delimiter='-')
    chris = [int(i) for i in chris]
except:
    chris = None
try:
    pca = np.loadtxt('initsols/C7'+'PCA.txt',dtype=int,delimiter='-')
    pca = [int(i) for i in pca]
except:
    pca = None
try:
    savings = np.loadtxt('initsols/C7' + 'SAVINGS.txt',dtype=int,delimiter='-')
    savings = [int(i) for i in savings]
except:
    savings = None
lis = [chris,pca,savings]
for i in lis:
    if i != None:
        b = Split('C7',permutation=i)
        print(len(b[0][0]))
        print(b[2])
    else:
        print('None')
        print('None')

