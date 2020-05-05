#!/bin/bash
#PBS -N blast
#PBS -l select=1:ncpus=10:mem=50gb:scratch_local=10gb
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add blast+-2.8.0a

datadir='/storage/brno3-cerit/home/kika/prototheca/wickerhamii/'
query=$datadir'pwic_hits.fa'
out=$datadir'pwic_hits.nr.blast.xml'
# db=$datadir'genome_db/pzop_genome.fa'
db='/storage/projects/BlastDB/nr'
program=tblastn
task=tblastn
outfmt=5
eval=1e-3
max_seqs=5

#run in DB folder
# cd $db_dir
$program -task $task \
	-query $query \
	-db $db \
	-out $out \
	-outfmt $outfmt \
	-num_threads $PBS_NUM_PPN \
	-evalue $eval \
	-max_target_seqs $max_seqs \
