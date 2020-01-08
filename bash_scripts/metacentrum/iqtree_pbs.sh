#!/bin/bash
#PBS -N IQTree
#PBS -q default
#PBS -l select=1:ncpus=15:mem=10gb:scratch_local=10gb:os=debian9
#PBS -l walltime=02:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.8

datadir='/storage/brno3-cerit/home/kika/pelomyxa/trees/fdhF/'

#copy files to scratch
cp $datadir'fdhF.trimal_0.5.aln' $SCRATCHDIR

#compute on scratch
cd $SCRATCHDIR
aln='fdhF.trimal_0.5.aln'
guide='guide_fdhF'
guide_tree=$guide'.treefile'
bb=1000

# iqtree -s $aln -bb $bb -nt AUTO -ntmax $PBS_NUM_PPN -m TEST -quiet

iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s $aln -pre $guide
iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s $aln -ft $guide_tree

#copy files back
rm $aln
cp * $datadir