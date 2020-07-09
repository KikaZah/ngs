#!/usr/bin/env python3
import os

os.chdir('/Users/kika/ownCloud/SAGs/phylogenomics/concatenated/ver7_full/LG4X_ufb/')
trees = [x for x in os.listdir() if x.endswith('.treefile')]

#file in format Acc. number \t name of organism \n
names = open('concat_names.txt')

name_dict = {}
for name in names:
	split_line = name.strip().split('\t')
	new = split_line[1]
	# new = split_line[1] + ' ' + split_line[0]
	name_dict[split_line[0]] = new

for tree in trees:
	print(tree)
	name = tree.split('.')[0]
	tree_line = open(tree).readline()
	for key in name_dict:
		tree_line = tree_line.replace(key, name_dict[key])
	with open('{}_renamed.tree'.format(name), 'w') as result:
		result.write(tree_line)
