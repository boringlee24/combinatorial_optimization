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

algos = ['steepest', 'bruteforce']
ALGOS = ['STEEPEST', 'EXHAUSTIVE']
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
            y_data[algo][index].append(output[i][0])

for ins in instances:
    index = instances.index(ins)
    axs[index].set_title(ins, fontsize=14)
    for algo in algos:
        x = np.array(x_data[algo][index])
        y = np.array(y_data[algo][index]) / max(y_data['steepest'][index])
        if algo == 'bruteforce':
            marker = 'd'
            color = 'deepskyblue'
        else:
            marker = 'o'
            color = 'orangered'
        ALGO = ALGOS[algos.index(algo)]
        axs[index].plot(x, y, label=ALGO, marker=marker, color=color)
        if index < 3:
            axs[index].yaxis.set_major_locator(MultipleLocator(0.25))
            axs[index].set_ylim(0,1.02)
        else:
            axs[index].yaxis.set_major_locator(MultipleLocator(0.25))
            axs[index].set_ylim(0,1.02)

        axs[index].xaxis.set_major_locator(MultipleLocator(10))
        axs[index].tick_params(axis = 'both', which='major', labelsize = 14)
        axs[index].grid(True, which='major', axis='both', linestyle='dashed')


handles, labels = axs[-1].get_legend_handles_labels()
#fig.legend(handles,labels,bbox_to_anchor=(0.49,0.45,0.5,.1), loc='center right', borderaxespad=0.1,handletextpad=0.3)
axs[-1].legend(fontsize=14)
fig.text(0.5, 0.05, 'Problem Size (Number of Subset Elements)', ha='center', va='center', fontsize=14)
axs[0].set_ylabel('Optimal Sum\n(Norm. SD Max)', fontsize=14)

plt.savefig('plots/steepest.pdf')

