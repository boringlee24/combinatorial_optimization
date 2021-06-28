import pandas
import pdb
from datetime import datetime
import matplotlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import glob
import sys
from matplotlib.ticker import MultipleLocator
import json
import os

algos = ['tabu_1min', 'tabu_10min']
ALGOS = ['TABU (1min)', 'TABU (10min)']
instances = ['P(3)', 'P(6)', 'EVEN/ODD', 'AVIS']
fig, axs = plt.subplots(1, 4, gridspec_kw={'hspace': 0.3, 'wspace': 0.3, 'bottom': 0.2, 'right':0.99, 'left':0.09}, figsize=(14,3))
x_data = {} # {greedy: [[1, 2, 3...], [], [], []], bf: [[1, 2, 3...], ...]}
y_data = {}
ins_size = 25

for algo in algos:
    x_data[algo] = []
    y_data[algo] = []
    path = f'{algo}.json'
    with open(path, 'r') as f:
        output = json.load(f)
    for index in range(0, 4):
        x_data[algo].append([])
        y_data[algo].append([])
        for i in range(index*ins_size, ins_size+index*ins_size):
            x_data[algo][index].append(output[i][1])
            y_data[algo][index].append(output[i][2])

for ins in instances:
    index = instances.index(ins)
    axs[index].set_title(ins, fontsize=14)
    for algo in algos:
        x = np.array(x_data[algo][index])
        y = np.array(y_data[algo][index])# / max(y_data['steepest'][index])
        if algo == 'tabu_1min':
            marker = 'd'
            color = 'deepskyblue'
        else:
            marker = 'o'
            color = 'orangered'
        ALGO = ALGOS[algos.index(algo)]
        axs[index].plot(x, y, label=ALGO, marker=marker, color=color)
        if index == 0 or index == 2:
#            axs[index].yaxis.set_major_locator(MultipleLocator(50))
            axs[index].set_ylim(0,1e5)
        else:
#            axs[index].yaxis.set_major_locator(MultipleLocator(100))
            axs[index].set_ylim(0,1e5)

        axs[index].xaxis.set_major_locator(MultipleLocator(10))
        axs[index].tick_params(axis = 'both', which='major', labelsize = 14)
        axs[index].grid(True, which='major', axis='both', linestyle='dashed')


handles, labels = axs[0].get_legend_handles_labels()
#fig.legend(handles,labels,bbox_to_anchor=(0.49,0.45,0.5,.1), loc='center right', borderaxespad=0.1,handletextpad=0.3)
axs[0].legend(fontsize=14, loc='upper left')
fig.text(0.5, 0.05, 'Problem Size (Number of Subset Elements)', ha='center', va='center', fontsize=14)
axs[0].set_ylabel('Number of Iterations', fontsize=14)

plt.savefig('plots/tabu_iter.pdf')

