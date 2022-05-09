import argparse
parser = argparse.ArgumentParser()
parser.add_argument("candidate",type=str)
parser.add_argument("busco",type=str)
parser.add_argument("vpf",type=str)
parser.add_argument("cat",type=str)
args = parser.parse_args()

def readset(filename):
    res = set()
    for line in open(filename,'r'):
        line = line.strip()
        res.add(line)
    return res

candidate = readset(args.candidate)
busco = readset(args.busco)
vpf = readset(args.vpf)
cat = readset(args.cat)

busco_filter = candidate.intersection(busco)
filter_final = busco_filter.difference(vpf)


valid = candidate.difference(filter_final).difference(cat)


outfile = open('valid_viral','w')

for ctgid in valid:
    outfile.write(ctgid+'\n')
outfile.close()





