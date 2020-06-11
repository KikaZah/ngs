#!/bin/bash
#PBS -N stampa
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=50gb
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

module add vsearch-1.4.4

data='/storage/brno3-cerit/home/kika/sl_euglenozoa/'
script='/storage/brno2/home/kika/scripts/kika/bash_scripts/metacentrum/v9_analysis/'

#copy files to scratch
cp $data'global_dereplicated_1f_representatives.fas' $SCRATCHDIR
cp $script'10b_chimera_detection.sh' $SCRATCHDIR

fasta='global_dereplicated_1f_representatives.fas'
chimera_sc='10b_chimera_detection.sh'


#compute on scratch
cd $SCRATCHDIR

# if [ $# != 1 ]; then
#     echo "You need to supply an input filename - *_1f_representatives.fas";
#     exit 1;
# fi

./$chimera_sc $fasta


#copy files back
rm $fasta $chimera_sc
cp -r * $data
