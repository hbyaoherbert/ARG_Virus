import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("ctgfile",type=str)
parser.add_argument("output",type=str)
args = parser.parse_args()

ctg2norf = {}
seqfile = open(args.ctgfile,'r')

for record in SeqIO.parse(seqfile,'fasta'):
    info = record.id.split('_')
    ctgid = info[0]+'_'+info[1]
    if ctgid in ctg2norf.keys():
        ctg2norf[ctgid] += 1
    else:
        ctg2norf[ctgid] = 1

outfile = open(args.output,'w')
for ctgid,num in ctg2norf.items():
    outfile.write(ctgid+'\t'+str(num)+'\n')
outfile.close()    
