import pdb
import numpy as np
import argparse
import random

# small scale input and large scale input generation options
parser = argparse.ArgumentParser(description='number of small and large scale inputs.')
parser.add_argument('--small', metavar='SMALL', type=int, default=50, help='an integer for the accumulator')
parser.add_argument('--large', metavar='LARGE', type=int, default=50, help='an integer for the accumulator')
args = parser.parse_args()

################ small scale generation ######################

item_n = [25, 50, 100, 200, 500]
weight_max = 100
bin_sizes = [100, 120, 150]
# bin_number will be Gaussian distributed with mean of item_n / (bin_size / (weight_max/2)) and var of 20% mean

input_f = open('input.txt', 'w')

num_small = args.small
for i in range(num_small):
    bin_size = random.choice(bin_sizes)
    item_num = random.choice(item_n)
    bin_num_mean = item_num / (bin_size / (weight_max / 2))
    bin_num_std = bin_num_mean * 0.2
    bin_num = int(np.random.normal(bin_num_mean, bin_num_std))
    item_size = np.random.uniform(1, weight_max, item_num).astype(int)
    w_line = f'{bin_size},{bin_num}'
    for val in item_size:
        w_line += f',{val}'
    w_line += ' \n'
    input_f.writelines(w_line)

################# large scale generation ########################

item_n = [100, 200, 500, 1000, 2000]
weight_max = 250
bin_sizes = [70, 100, 130, 160, 190, 220, 250]

num_large = args.large
for i in range(num_large):
    bin_size = random.choice(bin_sizes)
    item_num = random.choice(item_n)
    bin_num_mean = item_num / (bin_size / (weight_max / 2))
    bin_num_std = bin_num_mean * 0.2
    bin_num = int(np.random.normal(bin_num_mean, bin_num_std))
    item_size = np.random.uniform(1, weight_max, item_num).astype(int)
    w_line = f'{bin_size},{bin_num}'
    for val in item_size:
        w_line += f',{val}'
    w_line += ' \n'
    input_f.writelines(w_line)

input_f.close()

