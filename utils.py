from itertools import combinations


def interleave_zeros(lst):
    new_list = []
    for num in lst:
        new_list.extend([0, num])
    new_list.append(0)
    return new_list

def zeroindexes(x):
    zero_indexes = [i for i, x in enumerate(x) if x == 0]
    zero_indexes.pop(0)
    zero_indexes.pop(-1)
    return zero_indexes



def Zeroidx(Comroute):
    zero_indexes = [i for i, x in enumerate(Comroute) if x == 0]
    zero_indexes.pop(0)
    zero_indexes.pop(-1)
    return zero_indexes



def Splitfunc(completeroute,zero_indexes):
    """
    x = permutation  list
    y = interleave_zeros(x) list
    """
    steps = 1
    while steps <= len(zero_indexes) :
        lcombinations = list(combinations(zero_indexes, steps))
        for i in lcombinations:
            temp = completeroute.copy()
            o = list(i)
        #delete o as index from temp
            my_list = [temp[y] for y in range(len(temp)) if y not in i]
            ################ here will be a feasibility check and cost calculation
        steps = steps + 1

def NurseCons(zeroindexes, nurses, testcase):
    zero_indexes = zeroindexes(testcase)
    if len(zero_indexes) > nurses:
        a = False
    else:
        a = True
    return a


nurses = 2
testcase = [0,2,4,0,1,0,5,3,0]

def NurseCons(zeroindexes, nurses, testcase):
    zero_indexes = zeroindexes(testcase)
    if len(zero_indexes) > nurses:
        a = False
    else:
        a = True
    return a

z = NurseCons(zeroindexes, nurses, testcase)

print(z)




