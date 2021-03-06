#!/usr/bin/env python3
import subprocess
from Bio.Blast import NCBIXML

cmd = 'blastp'
task = 'blastp'
# query = '/Users/kika/ownCloud/diplonema/diff_expression/aminotransferases.D-_vs_D+.D-UP.fwd.fa'
query = '/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/search/enol.fa'
# db = '/Users/kika/ownCloud/diplonema/seq_data/dpapilatum/dpap_predicted_proteins.fa'
db = '/Users/kika/data/eukprot/EP00093_Oithona_nana.fasta'
# subject = '/home/kika/MEGAsync/diplonema_mt/1621/transcripts/y8/y8.fasta'
out = '/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/search/enol.EP00093.blast.xml'
evalue = 1
outfmt = 5
hits = 1
word_size = 3
threads = 6

print('running BLAST')
#query - database
subprocess.call('{} -task {} -query {} -db {} -out {} -evalue {} -outfmt {} -word_size {} \
	-num_threads {}'.format(
		cmd, task, query, db, out, evalue, outfmt, word_size, threads), shell=True)
# -max_target_seqs {} hits, 

# #query - subject
# subprocess.call('{} -query {} -subject {} -out {} -evalue {} -outfmt {} -word_size {}'.format(
# 		cmd, query, subject, out, evalue, outfmt, word_size), shell=True)

print('BLAST done')
print('writing BLAST results to tables')

result_handle = open(out)
blast_records = NCBIXML.parse(result_handle)
output = open('/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/search/enol.EP00093.blast.tsv', 'w')
out_best = open('/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution/opa1/search/enol.EP00093.best_blast.tsv', 'w')

output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'sseqdef',
	'slen', 'alen', 'evalue', 'frame', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 
	'alen_qlen', 'alen_slen'))
out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('qseqid', 'qlen', 'sseqid', 'sseqdef',
	'slen', 'alen', 'evalue', 'frame', 'pident', 'bitscore', 'mismatch', 'gaps', 'qstart', 'qend', 'sstart', 'send', 
	'alen_qlen', 'alen_slen'))

for record in blast_records:
	try:
		best_hit = record.alignments[0].hsps[0]
		# mismatches = best_hit.align_length - (best_hit.gaps + best_hit.positives)
		mismatches = best_hit.gaps + (best_hit.positives - best_hit.identities)
		pident = (best_hit.gaps+best_hit.identities)/best_hit.align_length*100
		alen_qlen = best_hit.align_length/record.query_length
		alen_slen = best_hit.align_length/record.alignments[0].length
		if best_hit.frame[1] > 0:
			# print(record.alignments[0].title)
			out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
				record.query, record.query_length, record.alignments[0].hit_id, record.alignments[0].hit_def, record.alignments[0].length, 
				best_hit.align_length, best_hit.expect, best_hit.frame[1], pident, best_hit.bits, mismatches, 
				best_hit.gaps, best_hit.query_start, best_hit.query_end, best_hit.sbjct_start, best_hit.sbjct_end, 
				alen_qlen, alen_slen))
		else:
			out_best.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
				record.query, record.query_length, record.alignments[0].hit_id, record.alignments[0].hit_def, record.alignments[0].length, 
				best_hit.align_length, best_hit.expect, best_hit.frame[1], pident, best_hit.bits, mismatches, 
				best_hit.gaps, best_hit.query_start, best_hit.query_end, best_hit.sbjct_end, best_hit.sbjct_start, 
				alen_qlen, alen_slen))
		for aln in record.alignments:
			for hsp in aln.hsps:
				# mismatches = hsp.align_length - (hsp.gaps + hsp.positives)
				mismatches = hsp.gaps + (hsp.positives - hsp.identities)
				pident = (hsp.gaps+hsp.identities)/hsp.align_length*100
				alen_qlen = hsp.align_length/record.query_length
				alen_slen = hsp.align_length/aln.length
				if hsp.frame[1] > 0:
					output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
						record.query, record.query_length, aln.hit_id, aln.hit_def, aln.length, hsp.align_length, hsp.expect,
						hsp.frame[1], pident, hsp.bits, mismatches, hsp.gaps, hsp.query_start, hsp.query_end, 
						hsp.sbjct_start, hsp.sbjct_end, alen_qlen, alen_slen))
				else:
					output.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(
						record.query, record.query_length, aln.hit_id, aln.hit_def, aln.length, hsp.align_length, hsp.expect, 
						hsp.frame[1], pident, hsp.bits, mismatches, hsp.gaps, hsp.query_start, hsp.query_end, 
						hsp.sbjct_end, hsp.sbjct_start, alen_qlen, alen_slen))
	except:
		pass
		output.write('{}\t{}\t***no hit found***\n'.format(record.query, record.query_length))
		out_best.write('{}\t{}\t***no hit found***\n'.format(record.query, record.query_length))
out_best.close()
output.close()
