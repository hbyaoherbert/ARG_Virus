import argparse

parser = argparse.ArgumentParser()
parser.add_argument("alnres",type=str)
parser.add_argument("annotation",type=str)
parser.add_argument("prot2tax",type=str)
args = parser.parse_args()

ctg2tax = {}
for line in open(args.annotation,'r'):
    line = line.strip()
    info = line.split('\t')
    ctg2tax[info[0]] = info[1]

prot2tax = {}
for line in open(args.prot2tax,'r'):
    line = line.strip()
    info = line.split('\t')
    prot2tax[info[0]] = info[1]

validset = set()
for line in open(args.alnres,'r'):
    line = line.strip()
    info = line.split('\t')
    orfinfo = info[0].split('_')
    ctgid = orfinfo[0]+'_'+orfinfo[1]
    if not ctgid in ctg2tax.keys():
            continue
  
    protacc = info[1].split('.')[0]
    if not protacc in prot2tax.keys():
        continue
 
    if prot2tax[protacc] != ctg2tax[ctgid]:
        continue
    evalue = float(info[10])
    
    if int(info[3])<20:
        continue
    validset.add(ctgid)

for ctg,tax in ctg2tax.items():
    if ctg in validset:
        print(ctg+'\t'+tax)
