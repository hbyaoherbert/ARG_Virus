import argparse
parser = argparse.ArgumentParser()
parser.add_argument('vpftab',type=str)
parser.add_argument('ctglist',type=str)
parser.add_argument('outprefix',type=str)

args = parser.parse_args()

tabfile = open(args.vpftab)
ctg2num = {}

ctgset = set()
for line in open(args.ctglist,'r'):
    line = line.strip()
    ctgset.add(line)

for line in tabfile:
    line = line.strip()
    if line[0] == '#':
        continue
    info = line.split(' ')
    rinfo = []
    for part in info:
        if len(part)>0:
            rinfo.append(part)
    if float(rinfo[4])<0.05:
        orfinfo = rinfo[0].split('_')
        ctgid = orfinfo[0]+'_'+orfinfo[1]


        if not ctgid in ctgset:
            continue

        if ctgid in ctg2num.keys():
            ctg2num[ctgid] += 1
        else:
            ctg2num[ctgid] = 1

outfile = open(args.outprefix+'.vpfhits','w')

for ctg in ctg2num.keys():
    if ctg2num[ctg] >=3 :
        outfile.write(ctg+'\n')
outfile.close()
