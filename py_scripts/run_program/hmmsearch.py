#!/usr/bin/env python3
import os
import subprocess

hmmsearch = '/Users/kika/miniconda3/bin/hmmsearch'

os.chdir('/Users/kika/ownCloud/archamoebae/import/hmms/')
files = [x for x in os.listdir() if x.endswith('.hmm')]

db = '/Users/kika/ownCloud/archamoebae/rhizomastix_libera_reassembly-IND8-VAV/rhizomastix_reassembly.trinity.NRfilt.faa'
orgn = 'rli_reas'
threads = 6

for file in files:
	print(file)
	name = file.split('.hmm')[0]
	out = orgn + '_' + name + '.hmm_search.table'
	subprocess.call('{} --tblout {} --cpu {} {} {}'.format(hmmsearch, out, threads, file, db), shell=True)
#-o
