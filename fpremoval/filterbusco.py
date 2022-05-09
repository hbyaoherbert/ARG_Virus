import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser()
parser.add_argument("hmmlist",type=str)
parser.add_argument("hmm2cut",type=str)
parser.add_argument("ctg2norf",type=str)
parser.add_argument("hmmsuffix",type=str)
parser.add_argument("outprefix",type=str)

args = parser.parse_args()

ctg2num = {}

def parsetab(tabfile,cut):
    tabfile = open(tabfile,'r')
    global ctg2num

    for line in tabfile:
        line = line.strip()
        if line[0] == '#':
            continue
        info = line.split(' ')
        rinfo = []


        for part in info:
            if len(part)>0:
                rinfo.append(part)
        if float(rinfo[4])<0.05 and float(rinfo[5])>=cut:
            #sample = rinfo[0].split('#')[-1]
            orfinfo = rinfo[0].split('_')
            ctgid = orfinfo[0]+'_'+orfinfo[1]
            if ctgid in ctg2num.keys():
                ctg2num[ctgid] += 1
            else:
                ctg2num[ctgid] = 1

def readcut(filename):
    scorecut = open(filename,'r')
    hmm2cut = {}
    for line in scorecut:
        line = line.strip()
        info = line.split('\t')
        hmm2cut[info[0]] = float(info[1])

    return hmm2cut

hmm2cut = readcut(args.hmm2cut)
hmmlist = open(args.hmmlist,'r')
for line in hmmlist:
    line = line.strip()
    info = line.split('\t')
    hmm = info[0].split('.')[0]
    cut = hmm2cut[hmm]
    parsetab('buscotab/'+hmm +'.hmm.'+args.hmmsuffix+'.tab',cut)



ctg2hitnum = {}

ctg2orfnum = {}
ctg2orf = open(args.ctg2norf,'r')
for line in ctg2orf:
    line = line.strip()
    info = line.split('\t')
    
    ctg2orfnum[info[0]] = int(info[1]) 



outfile = open(args.outprefix + '.buscohits','w')
for ctgid in ctg2num.keys():
   

    hits = ctg2num[ctgid]
   
    if not ctgid in ctg2orfnum.keys():
        continue

  
    ratio = hits/ctg2orfnum[ctgid]
    if ratio > 0.067:
        outfile.write(ctgid+'\n')

outfile.close()  

'''


for sample in sample2ctg.keys():
    ctgs = sample2ctg[sample]
    orf = open('/storage/holab/hbyao/rgiorf/'+sample+'.contigs.faa','r')
    ctg2orfnum = {}
    for record in SeqIO.parse(orf,'fasta'):
        orfinfo = record.id.split('_') 
        ctgid = orfinfo[0]+'_'+orfinfo[1]
        if ctgid in ctg2orfnum.keys():
            ctg2orfnum[ctgid] += 1
        else:
            ctg2orfnum[ctgid] = 1
    for ctgid in ctgs:
        ratio = ctg2hitnum[ctgid+'#'+sample]/ctg2orfnum[ctgid]
        if ratio > 0.067:
            print(ctgid+'#'+sample)

'''    
