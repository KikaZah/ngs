#!/bin/bash
#PBS -N cutadapt-vsearch
#PBS -l select=1:ncpus=1:mem=150gb:scratch_local=500gb
#PBS -l walltime=04:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add python36-modules-gcc
module add vsearch-1.4.4

data='/storage/brno3-cerit/home/kika/oil_sands/Lane26_18S_V9/'
merged=$data'merged_pear'
out=$data'trimmed_cutadapt'

#copy file to scratch
cp $merged/*.assembled.fastq $SCRATCHDIR
cp '/storage/brno2/home/kika/scripts/kika/bash_scripts/metacentrum/v9_analysis/2b_clean_fastq_files.sh' $SCRATCHDIR
# cp $sl'hashing.py' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
CUTADAPT_SCRIPT='2b_clean_fastq_files.sh'

export TMPDIR=$SCRATCHDIR

for f in *.assembled.fastq ; do
 # V4 or V9 as an option
 bash ${CUTADAPT_SCRIPT} ${f} V9
done

#copy files back
rm *.assembled.fastq '2b_clean_fastq_files.sh' #'hashing.py'
cp * $out
