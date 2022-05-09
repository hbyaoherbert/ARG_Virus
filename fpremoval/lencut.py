import argparse

from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("seqfile",type=str)
parser.add_argument("lencut",type=str)
parser.add_argument("outprefix",type=str)
args = parser.parse_args()

seqfile = open(args.seqfile,'r')
cut  = float(args.lencut)
outlong = open(args.outprefix+'.long.fa','w')
outshort = open(args.outprefix+'.short.fa','w')
longlist = open(args.outprefix+'.long','w')
shortlist = open(args.outprefix+'.short','w')
for record in SeqIO.parse(seqfile,'fasta'):
    if len(record.seq) >= cut:
        outlong.write('>'+record.id+'\n')
        outlong.write(str(record.seq)+'\n')
        longlist.write(record.id+'\n')
    else:
        outshort.write('>'+record.id+'\n')
        outshort.write(str(record.seq)+'\n')
        shortlist.write(record.id+'\n')

outlong.close()
outshort.close()
longlist.close()
shortlist.close()
    
