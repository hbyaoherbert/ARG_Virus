import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("prot2dna",type=str)
parser.add_argument("dna2tax",type=str)

args = parser.parse_args()

org2tax = {}
for line in open(args.dna2tax,'r'):
    line = line.strip()
    info = line.split('\t')
    org2tax[info[0]] = info[1]

prot2dnadf = pd.read_csv(args.prot2dna,sep=',',header=0)

for prot,org in zip(prot2dnadf["accession"],prot2dnadf["organism"]):
    if org in org2tax.keys():
        print(prot+'\t'+org2tax[org])





    
    
