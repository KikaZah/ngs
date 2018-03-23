#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/diplonema_mt/1601/transcripts/tadpole/y3/in'
one = 'NODE_295_length_22397_cov_76.2802'
positions = '13326-14500'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/1601_tadpole_renamed.fa'
out = '/home/kika/MEGAsync/diplonema_mt/1601/transcripts/tadpole/y3/out'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -range={} -strand={}'.format(one, db, out, positions, strand), 
# 	shell=True)