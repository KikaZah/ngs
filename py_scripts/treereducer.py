#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/home/kika/MEGAsync/diplonema/octopine_superfamily/fasttree/ver3/')
inacc = open('acc.delete.txt')
infasta = SeqIO.parse('ocdh_family_deduplicated.fa', 'fasta')

omitted = []
for line in inacc:
	omitted.append(line.strip())

c = 0
with open('ocdh_family_reduced.fa', 'w') as result:
	for seq in infasta:
		if seq.name in omitted:
			c += 1
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)