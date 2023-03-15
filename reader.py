import os
import sys

sys.path.append('MPMAVRPMain/Problem')
sys.path.append('Problem')
with open('MPMAVRPMain/Problem/A7.txt') as f:
   nurses = int(f.readline(1))
   patients = int(f.readline(2))
   TW = {}
   for i in range(patients):
    TW[i+3] = f.readline(i+3).split("\n")

print(TW)