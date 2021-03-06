#!/bin/bash
#PBS -N quast
#PBS -l select=1:ncpus=10:mem=3gb:scratch_local=5gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add quast-4.6.3

datadir='/storage/brno3-cerit/home/kika/pelomyxa/check-for-ncbi/'
outdir=$datadir'quast/'

#copy files to scratch
cp $datadir'pelomyxa_final_corr_genome.fa' $SCRATCHDIR

assemblies='pelomyxa_final_corr_genome.fa'
min_contig=500


#compute on scratch
cd $SCRATCHDIR
quast.py -o $SCRATCHDIR -t $PBS_NUM_PPN --glimmer --min-contig $min_contig --eukaryote $assemblies

# for fasta in $assemblies; do
# 	echo $fasta
# 	out=`echo $fasta | cut -d '.' -f 1`
# 	full_out=$outdir'/'$out

# 	quast.py -o $full_out -t $PBS_NUM_PPN --glimmer --min-contig $min_contig --eukaryote $fasta
# 	# cp -r * $full_out
# done


#copy results to your folder
# rm $f $bam
rm $assemblies
cp -r * $outdir
