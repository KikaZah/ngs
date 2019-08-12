#!/bin/bash

awk_path='/home/sebastian/extract/'
evm_path='/opt/evm/EVM_r2012-06-25/EvmUtils/'
data_dir='/home/kika/pelomyxa_schiedti/pasa-evm/'
evm=$data_dir'evm2/evm.all.gff3'
sorted=$data_dir'sorted.gff3'
deduplicated=$data_dir'sorted_deduplicated.gff3'
no_partials='sorted_deduplicated_no_partials.gff3'
renamed='renamed.gff3'
renamed2='renamed2.gff3'
final='pelomyxa_prediction_final.gff3'

# #sort the gff
# gff3_sort -g $evm -i -og $sorted
# echo '***Sorting gff done***'

# #remove duplicates since for unknown reason EVM makes some
# awk -f$awk_path'remove_duplicates_gff' $sorted > $deduplicated
# echo '***Deduplicating gff done***'

# #remove partials
# awk -f$awk_path'remove_partial_gff3' $missing $deduplicated > $no_partials
# echo '***Removing partials done***'

# #remove multiple lines of ### if exist
# cat $no_partials | uniq > removed
# mv removed $no_partials
# echo '***Removing lines of ### done***'

# #change EVM names in last columns
# awk -f awk_name.sh $no_partials > $renamed
# echo '***Change EVM names in last columns***'

# #removes Name=.* from last columns
# sed -E -i 's/Name=.*$//' $renamed
# echo '***Remove Name=.* from last columns***'

# #replaces the source of the prediction with PASA
# sed -E 's/(scaffold[0-9]+_[0-9]+\t)\EVM(\t)/\1PASA\2/' $renamed > $renamed2
# echo '***Replacing source with PASA***'

#corrects the parent issue in the gff file with mRNA
cat $renamed2 | awk -f $awk_path'fix_mRNA' > $final
echo '***Correcting parent issue done***'
