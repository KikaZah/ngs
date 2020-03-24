#!/usr/bin/env python3
import os
from Bio import SeqIO

os.chdir('/Dcko/ownCloud/proteromonas/RABs/tree/ver2/')
inacc = open('acc.delete')
infasta = SeqIO.parse('rabome_prot.fa', 'fasta')

omitted = []
for line in inacc:
	omitted.append(line.strip())

c = 0
with open('rabome_prot_reduced.fa', 'w') as result:
	for seq in infasta:
		if seq.description in omitted:
			c += 1
			print('{} in omitted list'.format(seq.name))
		else:
			result.write('>{}\n{}\n'.format(seq.description, seq.seq))
print(c)
