#!/bin/sh

workdir='/mnt/mokosz/home/kika/workdir/'
files=$workdir'*.fasta'
lineage=1
# 1) Mt
# 2) MRO
# 3) Piroplasma
# 4) Chlorophyta
# 5) Dictyostelium
# 6) Plasmodium
# 7) stramenopiles
# 8) Toxoplasma
# 9) Trypanosomatida

cd $workdir
for file in $files; do
	echo $file
	out=${file%.*}'.nommpred_mit.txt'
	NommPred.py -i $file -o $out -l $lineage --overwrite
done
