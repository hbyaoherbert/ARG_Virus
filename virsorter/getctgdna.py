from Bio import SeqIO
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("ctglist",type=str)
parser.add_argument("idlist",type=str)
parser.add_argument("ctgdir",type=str)
parser.add_argument("outprefix",type=str)
args = parser.parse_args()

dna = open(args.ctglist,'r')
ctgset = set()

for line in dna:
    ctgset.add(line.strip())

dna.close()

outfile = open(args.outprefix+'.fa','w')
for line in open(args.idlist,'r'):
    line = line.strip()
    seqfile = open(args.ctgdir+'/'+line+'.contigs.fa','r')
    for record in SeqIO.parse(seqfile,'fasta'):
        
        if record.id+'#'+line in ctgset:
            outfile.write('>'+record.id+'#'+line+'\n')
            outfile.write(str(record.seq)+'\n')

outfile.close()



