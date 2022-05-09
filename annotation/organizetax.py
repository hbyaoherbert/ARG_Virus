import argparse
import pandas as pd
parser = argparse.ArgumentParser()
parser.add_argument("taxdir",type=str)
parser.add_argument("output",type=str)

args = parser.parse_args()
taxmap = {}
levels = ['species','genus','family','order','class','phylum']
for level in levels:
    print(level)
    levelmap = {}
    taxfile = args.taxdir+'/org2'+level
    df = pd.read_csv(taxfile,sep='\t',header=None)
    df.columns = ['org',level]
    for org,tax in zip(df['org'],df[level]):
        if org in taxmap.keys():
            taxmap[org][level] = tax
        else:
            taxmap[org]={}
            taxmap[org][level] = tax

data = []
for org,levelmap in taxmap.items():
    org2tax = []
    for level in levels:
        if level in levelmap.keys():
            org2tax.append(levelmap[level])
        else:
            org2tax.append('not assigned')
    data.append(org2tax)

df = pd.DataFrame(data,columns=levels)
df.to_csv(args.output,sep='\t',index=False)    
