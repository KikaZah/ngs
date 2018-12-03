#!/usr/bin/python3
import subprocess

file = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/EG_prot/yoshida_dataset/gefr_acc.txt'
one = 'TRINITY_DN2240_c0_g1_i2'
positions = '43693-47247'
strand = 'plus'
db = '/home/kika/programs/blast-2.5.0+/bin/eg_tsa_Field.fasta'
out = '/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/EG_prot/yoshida_dataset/gefr_seqs2.fa'

subprocess.call('blastdbcmd -entry_batch {} -db {} -out {}'.format(file, db, out), shell=True)
# subprocess.call('blastdbcmd -entry {} -db {} -out {} -strand={}'.format(one, db, out, strand), 
# 	shell=True)

# -range={} 
# positions, 