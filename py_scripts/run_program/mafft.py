#!/usr/bin/env python3
import os
import subprocess

mafft = '/Users/kika/miniconda3/bin/mafft'

#align de-novo
os.chdir('/Users/kika/ownCloud/membrane-trafficking/trees/RABs/ver6/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	out = '{}.mafft.aln'.format(file.split('.fa')[0])
	log = '{}.mafft.log'.format(file.split('.fa')[0])
	subprocess.call('{} --thread 7 --localpair --maxiterate 1000 --inputorder {} > {} 2> {}'.format(
		mafft, file, out, log), shell=True)

# #add to aligned sequences
# os.chdir('/Users/kika/ownCloud/archamoebae/')
# existing = 'import/alns/Sam50.fas'
# add = 'trees/Sam50/sam50.fa'
# out = 'import/sam50-archam.mafft.aln'
# log = 'import/sam50-archam.mafft.log'
# subprocess.call('{} --add {} --thread 7 --inputorder {} > {} 2> {}'.format(mafft, add, existing, out, log), shell=True)
