import argparse
#python this.py acc2tax ctg2num_orf blastpres
import pandas as pd
parser = argparse.ArgumentParser()
parser.add_argument('prot2dna',type=str)
parser.add_argument('org2tax',type=str)
parser.add_argument('ctg_num_orf',type=str)
parser.add_argument('alnres',type=str)
args = parser.parse_args()

org2tax = {}
prot2tax = {}

def readtax(prot2dna,dna2tax):
    
    global org2tax
    global prot2tax
    for line in open(dna2tax,'r'):
        line = line.strip()
        info = line.split('\t')
        org2tax[info[0]] = info[1]

    protdf = pd.read_csv(prot2dna,sep=',',header=0)
   
    for prot, org in zip(protdf['accession'],protdf['organism']):
        if not org in org2tax.keys():
            continue
        prot2tax[prot] = org2tax[org]
    


    
        

def readnorf(filename):
    ctg2norf = {}
    for line in open(filename,'r'):
        line = line.strip()
        info = line.split('\t')
        ctg2norf[info[0]] = int(info[1])
    return ctg2norf

def checktax(ctg,assignments,ctg2norf):
    if len(assignments) == 0:
        return 'not'
    norf = ctg2norf[ctg]
    tax2num = {}
    num = 0
    for tax in assignments:
        num += 1
        if tax in tax2num.keys():
            tax2num[tax] += 1
        else:
            tax2num[tax] = 1
    tax2numlist = list(tax2num.items())
    tax2numlist = sorted(tax2numlist,key=lambda d:d[1],reverse=True)
   
    if tax2numlist[0][1]/norf >= 0.5:

        return tax2numlist[0][0]
    else:
        return 'not'

def sumtab(filename,ctg2norf):
    global prot2tax
   
    tabfile = open(filename,'r')
    ctg2tax = {}
    for line in tabfile:
        line = line.strip()
        info = line.split('\t')
        orfid = info[0]
        orfinfo = orfid.split('_')
        ctgid = orfinfo[0]+'_'+orfinfo[1]
        acc = info[1].split('.')[0]
        
        if not acc in prot2tax.keys():
            continue
        if ctgid in ctg2tax.keys():
            ctg2tax[ctgid].append(prot2tax[acc])
        else:
            ctg2tax[ctgid] = [ prot2tax[acc] ]

    for ctg,assignments in ctg2tax.items():
        taxassign = checktax(ctg,assignments,ctg2norf)
        if taxassign != 'not':
            print(ctg+'\t'+taxassign)         

readtax(args.prot2dna,args.org2tax)
ctg2norf = readnorf(args.ctg_num_orf)
sumtab(args.alnres,ctg2norf)

