import itertools
import random
from time import time
import pdb
import json
from joblib import Parallel, delayed
import os

input_f = open('input.txt', 'r')
rline = input_f.readlines()
input_f.close()

lp_opt = []
ilp_opt = []
for index,line in enumerate(rline):
    with open(f'cplex/lp_log/lp{index}.txt', 'r') as f:
        read = f.readlines()
        if 'optimal solution' not in read[1]:
            pdb.set_trace()
        else:
            obj = float(read[-2].strip().split(' = ')[1])
        lp_opt.append([obj, len(line.split(','))-1])
    with open(f'cplex/ilp_log/ilp{index}.txt', 'r') as f:
        read = f.readlines()
        if 'optimal integer solution' in read[1] or 'presolve' in read[0]:
            obj = float(read[-2].strip().split(' = ')[1])
        else:
            pdb.set_trace()
        ilp_opt.append([obj, len(line.split(','))-1])

with open('data/lp.json', 'w') as f:
    json.dump(lp_opt, f, indent=4)

with open('data/ilp.json', 'w') as f:
    json.dump(ilp_opt, f, indent=4)

