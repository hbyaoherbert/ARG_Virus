
python ctg_num_orf.py confident.orf.faa
python ctg_num_orf.py remain.orf.faa

nohup ./buscohmm.sh confident.orf.faa confident > busco_confident.log &
nohup ./buscohmm.sh remain.orf.faa remain > busco_remain.log &

nohup ./vpfhmm.sh confident.orf.faa confident > vpf_confident.log &
nohup ./vpfhmm.sh remain.orf.faa remain > vpf_remain.log


python filterbusco.py hmmlist scores_cutoff confident.orf.faa.norf confident confident
python filterbusco.py hmmlist scores_cutoff remain.orf.faa.norf remain remain
cat *.buscohits >> buscohits
  
python filtervpf.py confident.vpf.tab candidate.confident confident 
python filtervpf.py remain.vpf.tab candidate.remain remain
cat *.vpfhits >> vpfhits


