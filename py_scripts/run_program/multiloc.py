#!/usr/bin/env python3
import os
import subprocess

multiloc = '/home/kika/tools/MultiLoc2/src/multiloc2_prediction.py'

os.chdir('/home/kika/pelomyxa_schiedti/predicted_proteins/')
files = [x for x in os.listdir() if x.endswith('.fa')]

for file in files:
	print(file)
	name = file.split('.fa')[0]
	
	# option = 'animal'
	option = 'fungal'
	# option = 'plant'
	
	out = '{}.multiloc_{}.txt'.format(name, option)
	subprocess.call('python2 {} -fasta={} -origin={} -predictor=LowRes -result={} -output=simple'.format(
		multiloc, file, option, out), shell=True)
