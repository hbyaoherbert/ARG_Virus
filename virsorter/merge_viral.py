import argparse
parser = argparse.ArgumentParser()
parser.add_argument("virfinder_high",type=str)
parser.add_argument("virfinder_low",type=str)
parser.add_argument("virsorter_high",type=str)
parser.add_argument("virsorter_low",type=str)


args = parser.parse_args()

cat16 = open(args.virsorter_high,'r')
cat16set = set()
for line in cat16:
    line = line.strip()
    ctgid = line.split('\t')[0]
    cat16set.add(ctgid)

cat12 = open(args.virsorter_low,'r')
cat12set = set()
for line in cat12:
    line = line.strip()
    ctgid = line.split('\t')[0]
    cat12set.add(ctgid)

virlow = open(args.virfinder_low,'r')
virlowset = set()
for line in virlow:
    line = line.strip()
    ctgid = line.split('\t')[0]
    virlowset.add(ctgid)

virhigh = open(args.virfinder_high,'r')
virhighset = set()
for line in virhigh:
    line = line.strip()
    ctgid = line.split('\t')[0]
    virhighset.add(ctgid)

inter = virlowset.intersection(cat16set)

total = inter.union(cat12set).union(virhighset)

remain = cat12set.union(cat16set).union(virhighset).union(virlowset).difference(total)

confidentout = open(confident,'w')
remainout = open(remain,'w')
for ctg in total:
    confidentout.write(ctg+'\n')
for ctg in remain:
    remainout.write(ctg+'\n')

confidentout.close()
remainout.close()

