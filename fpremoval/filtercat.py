import argparse
from Bio import SeqIO
parser = argparse.ArgumentParser()
parser.add_argument("catres",type=str)
parser.add_argument("output",type=str)
args = parser.parse_args()




resfile = open(args.catres,'r')
outfile = open(args.output,'w')
next(resfile)
for line in resfile:
    line = line.strip()
    
    info = line.split('\t')
    ctgid = info[0]
    if info[1] == 'unclassified':
         continue
    if info[1] == 'no taxid assigned':
         continue
    if info[2] == 'no hits to database':
         continue
    #print(line)
    ratiostr = info[2].split(' ')[2]
    ratioinfo = ratiostr.split('/')
    ratio = int(ratioinfo[0])/int(ratioinfo[1])

    taxstr = info[3]
    taxinfo = taxstr.split(';')
    #if len(taxinfo) < 3:
        #continue
    #print(line,ratio)
   
    if taxinfo[1] != '10239':
        #if taxinfo[2] != '2' and taxinfo[2] != '2157' and taxinfo[2] != '2759':
            #continue
        
        outfile.write(line+'\n')

outfile.close()

    
    
