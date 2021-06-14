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

for index,line in enumerate(rline):
    num_var = len(line.split(',')) - 1
    str_list = []
    for i in range(num_var):
        str_list.append(f'x{i}') # [x1,x2,x3,x4]
    weight_list = line.split(',')
    cap = weight_list.pop(0)
    str_var = ' '.join(str_list) # x1 x2 x3 x4
    with open(f'cplex/p{index}.dat', 'w') as f:
        f.write(f'data;\n')
        f.write(f'set WEIGHTS := {str_var};\n')
        f.write(f'param:  cost :=\n')
        for var,weight in zip(str_list,weight_list):
            if var == str_list[-1]:
                f.write(f'  {var}  {weight.strip()};\n')
            else:
                f.write(f'  {var}  {weight.strip()}\n')
        f.write(f'param cap := {cap};')

    with open(f'cplex/lp{index}.file', 'w') as f:
        f.write(f'reset;\n')
        f.write(f'option solver cplex;\n')
        f.write(f'option cplex_options \'timelimit=600\';\n')
        f.write(f'model proj_lp.mod;\n')
        f.write(f'p{index}.dat;\n')
        f.write(f'solve;\n')
        f.write(f'display objective;')

    with open(f'cplex/ilp{index}.file', 'w') as f:
        f.write(f'reset;\n')
        f.write(f'option solver cplex;\n')
        f.write(f'option cplex_options \'timelimit=600\';\n')
        f.write(f'model proj_ilp.mod;\n')
        f.write(f'p{index}.dat;\n')
        f.write(f'solve;\n')
        f.write(f'display objective;')




