import sys
import matplotlib as plt
sys.path.append('butools2/Python')
sys.path.append('MPMAVRPMain/butools2/Python')
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
    
    def di(self):
        for i in range(self.D.shape[1]):
            num = -float((self.D[i,:].sum())) + 0.0
            if i == 0:
                d1 = np.matrix([num])
            else:
                d1 = np.concatenate((d1, np.matrix([num])), axis=0)
        return d1
    def sample(self):
        a = SamplesFromPH(self.pi,self.D,1)
        return a[0]

    
class phaseconvo():
    def __init__(self, First , Second):
        self.First = First
        self.Second = Second

    def pi(self):
        Conv = [self.First, self.Second]
        new = (1 - np.round(Conv[0].pi.sum(),2))*Conv[1].pi
        matnew = np.hstack((Conv[0].pi,new))
        return np.asmatrix(matnew)
    def D(self):
        #first create empty matrix
        cornerd = np.zeros((self.First.D.shape[1] +self.Second.D.shape[1] , self.First.D.shape[1] +self.Second.D.shape[1] ))
        #d1*pi 
        first = self.First.di() * self.Second.pi
        #replacement of first
        cornerd[0:self.First.D.shape[0],0:self.First.D.shape[1]] = self.First.D
        sec = self.First.di() * self.Second.pi
        cornerd[0:sec.shape[0],self.First.D.shape[0]:] = sec
        cornerd[sec.shape[0]:,(cornerd.shape[1] - self.Second.D.shape[1]):] = self.Second.D
        return np.asmatrix(cornerd)
    
    def Dist(self):
        if self.First == None:
            return self.Second
        elif self.Second == None:
            return self.First
        else:
            return phase(D=self.D(), pi=self.pi())
    
    
