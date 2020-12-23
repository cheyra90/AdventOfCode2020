from itertools import *
import numpy as np

fp = '1/input.txt'
dat = open(fp).read().strip().split('\n')
dat = [int(x) for x in dat]

cmb = list(combinations(dat, 2)) # get all combinations of pairwise combos

def is_valid(x):
    return sum(x) == 2020 # Check for validity 

ans = np.prod(list(filter(is_valid, cmb))) # apply the filter to the list of all combinations

print(ans)