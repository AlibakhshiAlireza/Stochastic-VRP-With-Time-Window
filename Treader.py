import numpy as np
a = np.loadtxt('Tiguchi\PSOAns.txt', delimiter=',',dtype='float')
for i in range(16):
    s = i*5
    print(a[s][-1],a[s+1][-1],a[s+2][-1],a[s+3][-1],a[s+4][-1])