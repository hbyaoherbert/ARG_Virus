import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("idlist",type=str)
parser.add_argument("virfinder_outdir",type=str)
parser.add_argument("outprefix",type=str)
args = parser.parse_args()
outprefix = args.outprefix
highout = open(outprefix+'.high','w')
lowout = open(outprefix+'.low','w')
def getsample(result):
    global highout
    global lowout
    sample = result.split('.')[0]
    csv = pd.read_csv(args.virfinder_outdir+'/'+result,header=0,sep=',')

    for name,score,p in zip(list(csv['name']),list(csv['score']),list(csv['pvalue'])):
        ctgid = name.split(' ')[0]

        if score>=0.9 and p<0.05:
            highout.write(ctgid+'#'+sample+'\t'+name+'\n')

        if score>=0.7 and p<0.05:
            lowout.write(ctgid+'#'+sample+'\t'+name+'\n')

def overlap(virsorter_fi,virfinder_fi):
    set1 = set()
    set2 = set()
    for line in open(virsorter_fi,'r'):
        set1.add(line.strip())
    for line in open(virfinder_fi,'r'):
        set2.add(line.strip())
    return list(set1.intersection(set2))



for line in open(args.idlist,'r'):
    getsample(line.strip()+'.csv')

highout.close()
lowout.close() 
