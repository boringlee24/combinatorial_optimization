import numpy
import seaborn as sns
import matplotlib.pylab as plt
import matplotlib.pylab as mp
import statistics
from matplotlib import gridspec
import statistics
import pdb
import json
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')

def mapping(x):
    if x < 0:
        out = -1
    elif x == 0:
        out = 0
    else:
        out = 1
    return out

instances = ['P(3)', 'P(6)', 'EVEN/ODD', 'AVIS']
space = np.zeros((len(instances),25))

y_data = []
path_bf = f'bruteforce.json'
path_gd = f'greedy.json'
with open(path_bf, 'r') as f:
    output_bf = json.load(f)
with open(path_gd, 'r') as f:
    output_gd = json.load(f)
ins_size = 25

for index in range(0, 4):
    for i in range(index*ins_size, ins_size+index*ins_size):
        out = mapping(output_gd[i][0] - output_bf[i][0])
        space[index,i%25] = out

subplotnum=1
xticks = np.asarray(range(2, 52, 2))
yticks = ['P(3)', 'P(6)', 'EV/OD', 'AVIS']

fig, ax = plt.subplots(1, 1, gridspec_kw={'hspace': 0.3, 'wspace': 0.3, 'bottom': 0.2, 'right':0.99, 'left':0.09}, figsize=(14,3))
res=sns.heatmap(space,linewidth=0.5,cbar=False, cmap='PiYG',linecolor='black')
#ax.set_ylabel(labelpad=0.2)
for _, spine in res.spines.items():
    spine.set_visible(True)
#ax.set_xticks(xticks)
#plt.xticks(ha='center')
#ax.set_yticks(yticks)
#ax.set_yticklabels(yticks, ha='center')
ax.set_xticklabels(xticks, fontsize=14)
ax.set_yticklabels(yticks, ha='right', va='center', fontsize=14, rotation='horizontal')
ax.set_title('Colormap of Greedy vs. Exhaustive', fontsize=16)
ax.set_xlabel('Problem Size (Number of Subset Elements', fontsize=16)
mp.savefig('plots/heatmap.pdf',bbox_inches='tight')
