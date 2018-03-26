#!/usr/bin/python3
import os

os.chdir('/media/4TB1/blastocrithidia/orthofinder/other_ogs/stops_replaced/')
files = os.listdir()

for file in files:
	if file.endswith('2.fa'):
	# if '.aln' not in file:
		print(file)
		job_desc = file.split('_')[0]
		d = 'protein'
		os.system('run_pasta.py -i {} -d {} -j {}'.format(file, d, job_desc))