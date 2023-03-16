import numpy as np
import sys
sys.path.append('butools2/Python')
sys.path.append('MPMAVRPMain/butools2/Python')
import pickle	
from butools.fitting import *
from butools.ph import *
from phase import *


# Getting back the objects:
with open('objs.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    TravelTimeDist,ServiceTimeDist = pickle.load(f)
  
