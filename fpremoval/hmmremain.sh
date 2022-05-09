for i in `cat hmmlist`
do
    hmmsearch --tblout crcbusco_remain/${i}.tab --cpu 24 hmms/$i $1
done 
