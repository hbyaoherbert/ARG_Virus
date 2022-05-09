python filterbusco.py hmmlist scores_cutoff confident.orf.faa.norf confident confident
python filterbusco.py hmmlist scores_cutoff remain.orf.faa.norf remain remain
cat *.buscohits >> buscohits
  
python filtervpf.py confident.vpf.tab confident confident
python filtervpf.py remain.vpf.tab remain remain
cat *.vpfhits >> vpfhits

python script/sumviral.py candidate buscohits vpfhits cathits
python script/getctgdna.py valid_viral candidate.fa valid_viral 
