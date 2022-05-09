#bdir="~/busco/data/bacteria_odb9/"
orfdir="../virsorter/"
for i in `cat hmmlist`
do
    hmmsearch --tblout buscotab/${i}.${2}.tab --cpu 12 buscohmm/$i ${orfdir}/${1}
done 
