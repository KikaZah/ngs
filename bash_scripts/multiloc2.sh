#!/bin/sh

f="/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Tetrapyrrole/in"
r="/home/kika/MEGAsync/Euglena_longa/2013_Sekvenovanie/Tetrapyrrole/in_multiloc.txt"
a=animal
p=plant

/usr/bin/python2.7 /home/kika/programs/MultiLoc2-26-10-2009/src/multiloc2_prediction.py -fasta=$f -predictor=LowRes -origin=$a -result=$r -output=simple
