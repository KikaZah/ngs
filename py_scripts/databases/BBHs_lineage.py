#!/usr/bin/env python3
import os
from Bio import Entrez, SeqIO
from collections import defaultdict

Entrez.email = 'kika.zahonova@gmail.com'

os.chdir('/mnt/mokosz/home/kika/prototheca/')
table = 'pwic_hits.nr.blast.tsv'
output = 'pwic_hits.taxonomy_assigned.tsv'
errors = open('pwic_hits.tax_errors.txt', 'w')

def taxonomy_assign(accs, database, errors):
	final = set()
	for acc in accs:
		try:
			sequence = Entrez.efetch(db=database, id=acc, rettype='gb', retmode='text')
			record = SeqIO.read(sequence, 'genbank')
			tax = record.annotations['taxonomy'][1]
			final.add(tax)
		except:
			errors.write('{}\n'.format(acc))
	final = str(final).replace('{', '').replace('}', '').replace('\'', '')
	return final


accessions = defaultdict(set)
for line in open(table):
	query = line.split('\t')[0].split(' ')[0]
	subject = line.split('\t')[2].strip()
	if subject == 'sseqid':
		pass
	elif subject == '***no hit found***':
		pass
	else:
		subject = subject.split('|')[3]
		accessions[query].add(subject)

with open(output, 'w') as out:
	for query, accs in accessions.items():
		print(query)
		taxonomy = taxonomy_assign(accs, 'protein', errors)
		out.write('{}\t{}\n'.format(query, taxonomy))
