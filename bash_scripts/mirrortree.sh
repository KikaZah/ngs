#!/bin/bash

mt='/Users/kika/programs/MirrorTree/mirrortree_mac-uni'
matrix='/Users/kika/programs/MirrorTree/Maxhom_McLachlan.metric'
aln='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution-test/concat_enol_mic60.aln'
out='/Users/kika/ownCloud/Mic60-Mgm1-Opa1/coevolution-test/concat_enol_mic60.MT.txt'
first=536
second=1382

$mt $aln $matrix $first $second 2> $out 1> $out
