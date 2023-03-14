import sys
import matplotlib as plt
sys.path.append('butools2/Python')
from butools.ph import *
import numpy as np
a = np.matrix([[0.1,0.9,0]])
A = np.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
x = np.arange(0.0,3.002,0.002)

class phase():
    def __init__(self, D , pi):
        self.D = D
        self.pi = pi
        

    def GreaterThan(self, x):
        a = [x]
        return 1 - CdfFromPH(self.pi,self.D, a)[0]
    
    def LessThan(self, x):
        a = [x]
        return CdfFromPH(self.pi,self.D, a)[0]
    
    def between(self, x, y):
        a = [x]
        b = [y]
        return self.GreaterThan(a) - self.GreaterThan(b)
    
class phaseconvo():
    def __init__(self, First , Second):
        self.First = First
        self.Second = Second

    def pi(self):
        Conv = [self.First, self.Second]
        new = (1 - np.round(Conv[0].pi.sum(),2))*Conv[1].pi
        matnew = np.hstack((Conv[0].pi,new))
        return matnew
    
    
if __name__ == "__main__" :
    pi = np.matrix([[0.1,0.9,0]])
    D = np.matrix([[-6.2, 2, 0],[2, -9, 1],[1, 0, -3]])
    ph = phase(D=D, pi=pi)
    print(ph.GreaterThan(1))
