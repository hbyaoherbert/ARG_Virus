import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("annotation",type=str)
parser.add_argument("seqfile",type=str)
args = parser.parse_args()

ctgset = set()
for line in open(args.annotation,'r'):
    line = line.strip()
    info = line.split('\t')
    ctgset.add(info[0])

seqfile = open(args.seqfile,'r')
for record in SeqIO.parse(seqfile,'fasta'):
    if record.id in ctgset:
        print('>'+record.id)
        print(str(record.seq))


