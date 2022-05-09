for i in `cat $1`
do
    prodigal -i $i -p meta -a ${i}.orf.faa -d ${i}.orf.fa -q &
done

