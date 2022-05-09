from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ctglist",type=str)
parser.add_argument("ctgfile",type=str)
parser.add_argument("outprefix",type=str)
args = parser.parse_args()

dna = open(args.ctglist,'r')
ctgset = set()

for line in dna:
    ctgset.add(line.strip())

dna.close()

outfile = open(args.outprefix+'.fa','w')
seqfile = open(args.ctgfile,'r')
for record in SeqIO.parse(seqfile,'fasta'):        
    if record.id in ctgset:
        outfile.write('>'+record.id+'\n')
        outfile.write(str(record.seq)+'\n')

outfile.close()



