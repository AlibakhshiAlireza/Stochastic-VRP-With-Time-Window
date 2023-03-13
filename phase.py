import sys
import matplotlib as plt
sys.path.append('butools2/Python')
from butools.ph import *
import numpy as np
a = np.matrix([[0.1,0.9,0]])
A = np.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
x = np.arange(0.0,3.002,0.002)
cdf = CdfFromPH(a, A, x)
print(cdf)