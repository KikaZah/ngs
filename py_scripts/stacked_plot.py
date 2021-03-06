#!/usr/bin/env python3
import os
import pandas as pd
import matplotlib.pyplot as plt

# os.chdir('/Users/kika/ownCloud/SL_Euglenozoa/V9/V9DS_identities/')
# df = pd.read_csv('otu_identities.tsv', sep='\t')
# # print(df)

# #SL_Euglenozoa
# colors = ['#000000', '#CD950B', '#FFB90F', '#FFFF99', '#FAEBD7', 
# 	'#CAB2D6', '#FB9A99', '#B2DF8A', '#009444', '#1F78B4',
# 	'#C9C9C9', '#BCDEB4', '#7FFFD4', '#A6CEE3']

# # #oil sands
# # colors = ['#999999', '#000000', '#FFFF99', '#FAEBD7', 
# # 	'#CAB2D6', '#FB9A99', '#B2DF8A', '#009444', '#1F78B4',
# # 	'#C9C9C9', '#7FFFD4', '#A6CEE3']

# ax = df.plot(x='perc', kind='bar', stacked=True, color=colors, width=0.5, align='center')
# ax.set_xticklabels(df.perc, rotation=0)
# ax.xaxis.set_tick_params(width=0.5)
# ax.yaxis.set_tick_params(width=0.5)
# ax.set_xlabel('Similarity to reference sequences [%]')
# ax.set_ylabel('OTU count')
# ax.yaxis.grid(True, which='major', linestyle='-', linewidth=0.25)
# ax.set_axisbelow(True)
# ax.spines['right'].set_visible(False)
# ax.spines['left'].set_linewidth(0.6)
# ax.spines['top'].set_visible(False)
# ax.spines['bottom'].set_linewidth(0.6)
# ax.legend(bbox_to_anchor=(1, 1), frameon=False)
# plt.tight_layout()
# # plt.show()
# plt.savefig('otu_identities.pdf', dpi=300)


os.chdir('/Users/kika/ownCloud/oil_sands/Lane26_18S_V9/supergroups/')
df = pd.read_csv('supergroups-noOct10-2018-P3S_S72.tsv', sep='\t')
# print(df)

# #SL_Euglenozoa
# colors = ['#000000', '#CD950B', '#FFB90F', '#FFFF99', '#FAEBD7', 
# 	'#CAB2D6', '#FB9A99', '#B2DF8A', '#009444', '#1F78B4',
# 	'#C9C9C9', '#BCDEB4', '#7FFFD4', '#A6CEE3']

#oil sands
colors = ['#999999', '#000000', '#FFFF99', '#FAEBD7', 
	'#CAB2D6', '#FB9A99', '#B2DF8A', '#009444', '#1F78B4',
	'#C9C9C9', '#7FFFD4', '#A6CEE3']

ax = df.plot(x='sample', kind='barh', stacked=True, color=colors, width=0.5, align='center')
ax.set_xlabel('OTU count', fontsize=6)
ax.set_ylabel('sample', fontsize=6)
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
ax.xaxis.set_tick_params(width=0.5)
ax.yaxis.set_tick_params(width=0.5)
ax.xaxis.grid(True, which='major', linestyle='-', linewidth=0.25)
ax.invert_yaxis()
ax.set_axisbelow(True)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.6)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.6)
ax.legend(bbox_to_anchor=(1, 1), loc=2, fontsize=6, frameon=False)
plt.tight_layout()
# plt.show()
plt.savefig('supergroups-noOct10-2018-P3S_S72.pdf', dpi=300)
