from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ctglist")
parser.add_argument("ctgfile")
args = parser.parse_args()

ctgmap = {}
for line in open(args.ctglist,'r'):
    line = line.strip()
    info = line.split('\t')
    ctgmap[info[0]] = info[1]

seqfile = open(args.ctgfile,'r')
for record in SeqIO.parse(seqfile,'fasta'):
    if record.id in ctgmap.keys():
        print(record.id+'\t'+str(len(record.seq)) +'\t'+ ctgmap[record.id])



