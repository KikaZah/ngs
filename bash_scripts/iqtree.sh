#!/bin/bash

aln='/home/kika/ownCloud/pelomyxa/mito_proteins/pyruvate_metabolism/hydA_tree/hydA_trimal_automated1.aln'
bb=1000
alrt=5000
nm=5000

iqtree-omp -s $aln -bb $bb -nt 4 -m TEST

# -alrt $alrt -nm $nm