import pdb
import numpy as np
import argparse
import random

def gen(lower, upper, cap_co, input_f):
    for n in range(5, 101, 5):
        cap = int(n * cap_co)
        wline = f'{cap}'
        weights = np.random.randint(lower, upper, size=n)
        for w in weights:
            wline += f',{w}'
        wline += '\n'
        input_f.writelines(wline)

input_f = open('input.txt', 'w')

################ P3 ######################

lower = 1
upper = 1e3
cap_co = 1e3 / 4
gen(lower, upper, cap_co, input_f)

############### P6 ####################

lower = 1
upper = 1e6
cap_co = 1e6 / 4
gen(lower, upper, cap_co, input_f)

############### EVEN/ODD ####################

lower = 1
upper = 1e3

for n in range(5, 101, 5):
    cap = int(n * 1e3 / 4 + 1)
    wline = f'{cap}'
    weights = np.random.randint(lower, upper, size=n)
    for w in weights:
        wline += f',{w}'
    wline += '\n'
    input_f.writelines(wline)

############### AVIS ####################

for n in range(5, 101, 5):
    cap = int(n * (n+1) * (n-1) / 2 + n * (n-1) / 2)
    wline = f'{cap}'
    weights = [n * (n+1) + j for j in range(n)] 
    for w in weights:
        wline += f',{w}'
    wline += '\n'
    input_f.writelines(wline)

############### TODD ####################

for n in range(5, 26, 1):
    weights = [n * (2**(n+1)) + n * (2**j) + 1 for j in range(n)] 
    cap = int(sum(weights) / 2)
    wline = f'{cap}'
    for w in weights:
        wline += f',{w}'
    wline += '\n'
    input_f.writelines(wline)

input_f.close()


