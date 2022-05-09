#diamond 0.9.34
ctg=$1
protein_orf=$2
output=$3

CAT contigs --force -d /storage/holab/hbyao/cat/CAT_prepare_20200618/2020-06-18_CAT_database/ -t /storage/holab/hbyao/cat/CAT_prepare_20200618/2020-06-18_taxonomy/ -c $1  -p $2 -n 24 -o $3

