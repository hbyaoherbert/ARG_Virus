import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("ctglist",type=str)
parser.add_argument("orffile",type=str)
parser.add_argument("outprefix",type=str)

args = parser.parse_args()
ctgset = set()
for line in open(args.ctglist,'r'):
    ctgset.add(line.strip())

outfile = open(args.outprefix+'.faa','w')
seqfile = open(args.orffile,'r')
for record in SeqIO.parse(seqfile,'fasta'):
    info = record.id.split('_')
    ctgid = info[0]+'_'+info[1]
    if ctgid in ctgset:
        outfile.write('>'+record.id+'\n')
        outfile.write(str(record.seq)+'\n')
outfile.close()

