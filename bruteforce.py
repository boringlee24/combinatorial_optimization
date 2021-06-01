import itertools
import random
from time import time
import pdb
import json
from joblib import Parallel, delayed
import os

def bruteforce(x_list, target):
    optimal = 0
    for x in powerset(x_list):
        total = sum(x)       
        if total >= optimal and total <= target:
            optimal = total
    return optimal 

def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))

def inner_loop(line):
#    pdb.set_trace()
    split = line.split(',')
    target = int(split.pop(0))
    split[-1] = split[-1].replace('\n','')
    x_list = [int(i) for i in split]

    bf = bruteforce(x_list, target)
    return (bf, len(x_list))

def main():
    x_list = []
    for i in range(0,5):                        
        num = random.randint(0,100)               
        x_list.append(num) 

    target = random.randint(0,100) 

    input_f = open('input.txt', 'r')
    rline = input_f.readlines()
    input_f.close()

    usable_cores = os.sched_getaffinity(0)
    bf_opt = Parallel(n_jobs=len(usable_cores))(delayed(inner_loop)(line) for line in rline)
    with open(f'data/bruteforce.json', 'w') as f:
        json.dump(bf_opt, f, indent=4)

if __name__ == '__main__':
    main()
