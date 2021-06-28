import itertools
import random
from time import time
import pdb
import json
from joblib import Parallel, delayed
import os
import numpy as np

def eval_sol(sol, x_list):
    total = sum(np.multiply(np.array(sol), np.array(x_list)))
    return int(total)

def rand_init(x_list, target):
    while True:
        sol = []
        for x in x_list:
            sol.append(random.choice([1, 0]))
        total = eval_sol(sol, x_list)
        if total <= target:
            return sol

def tabu(x_list, target):
    init_sol = rand_init(x_list, target)
    init_sum = eval_sol(init_sol, x_list)
    best_neigh = init_sol[:]
    best_sum = init_sum
    start_t = time()
    time_lim = 60
    num_iter = 0
    tabu_len = 100
    tabu = []
    tabu.append(init_sol)
    # explore neighbors
    while True:
        exp_neigh = [] # [[1,0,1],[1,1,1],...]
        exp_sum = [] # [100, 50,...]
        curr_neigh = best_neigh[:]
        for ind, x in enumerate(curr_neigh):
            new_neigh = curr_neigh[:]
            if x == 1:
                new_neigh[ind] = 0
            else:
                new_neigh[ind] = 1
            if new_neigh not in tabu:
                neigh_sum = eval_sol(new_neigh, x_list)
                num_iter += 1
                tabu.append(new_neigh)
                exp_neigh.append(new_neigh)
                exp_sum.append(neigh_sum)
#                if neigh_sum >= best_sum and neigh_sum <= target:
#                    # this is a better solution in neighborhood
#                    best_sum = neigh_sum
#                    best_neigh = new_neigh[:]
        filtered = [k for k in exp_sum if k <= target]
        if len(filtered) == 0:
            return[best_sum, num_iter]
        else:
            local_best = max(filtered)
            if local_best >= best_sum:
                best_sum = local_best
            # choose next next neighbor
            best_index = exp_sum.index(local_best)
            best_neigh = exp_neigh[best_index][:]
        if time() - start_t > time_lim:
            return [best_sum, num_iter]
        
def inner_loop(line, index):
    split = line.split(',')
    target = int(split.pop(0))
    split[-1] = split[-1].replace('\n','')
    x_list = [int(i) for i in split]

    gd = tabu(x_list, target)
    print(f'finished line {index}')
    return (gd[0], len(x_list), gd[1])

def main():
    input_f = open('input.txt', 'r')
    rline = input_f.readlines()
    input_f.close()

    usable_cores = os.sched_getaffinity(0) 
    gd_opt = Parallel(n_jobs=len(usable_cores))(delayed(inner_loop)(line, rline.index(line)) for line in rline)
    with open(f'data/tabu.json', 'w') as f:
        json.dump(gd_opt, f, indent=4)

if __name__ == '__main__':
    main()
