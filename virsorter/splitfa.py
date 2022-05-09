import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("fasta",type=str)
parser.add_argument("nproc",type=str)
parser.add_argument("outprefix",type=str)
args = parser.parse_args()

seqfile = open(args.fasta,'r')
records = []
data = {}
for record in SeqIO.parse(seqfile,'fasta'):
    records.append(record.id)
    data [record.id] = str(record.seq)


N = len(records)
nproc = int(args.nproc)
proc2jobs = {}
for i in range(nproc):
    proc2jobs[i] = []
for i in range(N):
    idx = i % nproc
    proc2jobs[idx].append(records[i])

for i in range(nproc):
    outfile = open(args.outprefix+str(i)+'.fa','w')
    for job in proc2jobs[i]:
        outfile.write('>'+job+'\n')
        outfile.write(data[job]+'\n')
    outfile.close()

