import argparse
from Bio import SeqIO
import os
parser = argparse.ArgumentParser()
parser.add_argument("idlist",type=str)
parser.add_argument("virsorterout",type=str)
#parser.add_argument("outdir",type=str)
args = parser.parse_argument()
resdir = args.virsorterout

def fetchctgid(filename):
    seqfile = open(filename,'r')
    res = []
    for record in SeqIO.parse(seqfile,'fasta'):
        res.append(record.id)
    return res

def getsample(sample):
    output = resdir+'/'+sample+'/Predicted_viral_sequences/'
    cat1 = output+'VIRSorter_cat-1.fasta'
    cat2 = output+'VIRSorter_cat-2.fasta'
    res1 = fetchctgid(cat1)
    res2 = fetchctgid(cat2)
    outfile = open('cat12/'+sample+'.12','w')
    for ctg in res1:
        outfile.write(ctg+'\n')
    for ctg in res2:
        outfile.write(ctg+'\n')
    outfile.close()

def getsample16(sample):
    output = resdir + '/'+sample+'/Predicted_viral_sequences/'
    outfile = open('cat16/'+sample+'.16','w')
    for filename in os.listdir(output):
        if filename.find('fasta') <0:
            continue
        cat = output+filename
        
        res = fetchctgid(cat)
  
        for ctg in res:
            outfile.write(ctg+'\n')
    
    outfile.close()

for line in open(args.idlist,'r'):
    getsample(line.strip())
    getsample16(line.strip())
    
