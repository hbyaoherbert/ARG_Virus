python getvirsorter.py idlist $1
python getctgid.py idlist
python merge_viral.py virfinder.high virfinder.low virsorter.high virsorter.low 
python getctgdna.py confident idlist $2 confident
python getctgdna.py remain idlist $2 confident

#split fasta files to accelerate prodigal
python splitfa.py confident.fa 12 temp/confident
python splitfa.py remain.fa 12 temp/remain
ls temp/confident* > listc
ls temp/remain* > listr
nohup predictorf.sh listc &
nohup predictorf.sh listr &




#Wait the above commands finish