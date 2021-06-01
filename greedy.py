import itertools
import random
from time import time
import pdb
import json
from joblib import Parallel, delayed
import os

def greedy(x_list, target):
    # sort all inputs from large to small
    # add in numbers from large to small if fit. It not fit, don't add
    # greedy algorithm runs in O(n) time
    optimal = 0
    x_list.sort(reverse=True)
    for x in x_list:
        if optimal + x <= target:
            optimal += x
        if optimal == target:
            break
    return optimal 

def inner_loop(line):
#    pdb.set_trace()
    split = line.split(',')
    target = int(split.pop(0))
    split[-1] = split[-1].replace('\n','')
    x_list = [int(i) for i in split]

    gd = greedy(x_list, target)
    return (gd, len(x_list))

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
    gd_opt = Parallel(n_jobs=len(usable_cores))(delayed(inner_loop)(line) for line in rline)
    with open(f'data/greedy.json', 'w') as f:
        json.dump(gd_opt, f, indent=4)

if __name__ == '__main__':
    main()
