#!/bin/bash
#PBS -N iqtree
#PBS -l select=1:ncpus=20:mem=20gb:scratch_local=1gb:os=debian9
#PBS -l walltime=24:00:00
#PBS -m ae
#PBS -j oe

cat $PBS_NODEFILE

#add module
module add iqtree-1.6.12

data_dir='/storage/brno3-cerit/home/kika/sags/mit/ver4/concat_eug_bs'

#copy files to scratch
cp $data_dir'/'*.aln $SCRATCHDIR


#compute on scratch
cd $SCRATCHDIR

for f in *.aln ; do
 # guide=guide_${f%.trimal_0.5.aln}
 # guide_tree=$guide'.treefile'
 bb=1000
 iqtree -m TEST -nt AUTO -ntmax $PBS_NUM_PPN -b $bb -quiet -s ${f}
 # iqtree -m LG+F+G -nt AUTO -ntmax $PBS_NUM_PPN -quiet -s ${f} -pre $guide
 # iqtree -m LG+C20+F+G -nt AUTO -ntmax $PBS_NUM_PPN -bb $bb -quiet -s ${f} -ft $guide_tree
done

#copy files back
rm *.aln
cp * $data_dir