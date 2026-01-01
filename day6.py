import numpy as np
import math

# PART 1
inp = open('input6.txt', 'r').read().split('\n')
signs = inp[-1].split()
inp = inp[:-1]
npinp = np.array([l.split() for l in inp])
nums = npinp.T
total = 0
for i in range(len(nums)):
    if signs[i] == '*':
        total += np.prod(nums[i].astype(int))
    elif signs[i] == '+':
        total += np.sum(nums[i].astype(int))
print(total)

# PART 2
total2 = 0
k = 0
blockval = 0
plormu = False
if signs[k] == '*':
    plormu = True
blockval = 1 if plormu else 0
for i in range(len(inp[0])):
    allspaces = True
    colnum = 0
    f = 0
    for j in range(len(inp)-1, -1, -1):
        if inp[j][i] != ' ':
            allspaces = False
            colnum += (int(inp[j][i]) * (10 ** f))
            f += 1
    if allspaces:
        # add to the total2
        # print("blockval at ", i, "is ", blockval)
        total2 += blockval
        # update to next block
        k += 1
        if signs[k] == '*':
            plormu = True
        else:
            plormu = False
        blockval = 1 if plormu else 0
        continue
    if plormu:
        blockval *= colnum
        # print("adding colnum ", colnum, "to curr blockval for ", k, "giving blockval", blockval)
    else:
        blockval += colnum
    #     print("adding colnum ", colnum, "to curr blockval for ", k, "giving blockval", blockval)
    # print("finished loop at iter i", i)
total2 += blockval # add residual last blockvalue
print(total2)
