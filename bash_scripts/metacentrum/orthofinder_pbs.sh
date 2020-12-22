#!/bin/sh
#PBS -N orthofinder
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=5gb
#PBS -l walltime=336:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add orthofinder-2.0.0

data='/storage/brno3-cerit/home/kika/archamoebae'


#copy files to scratch
cp $data'/'*prot* $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

orthofinder -f $SCRATCHDIR

#copy files back
rm *prot*
cp -R * $data
