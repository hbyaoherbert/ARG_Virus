import argparse

parser = argparse.ArgumentParser()
parser.add_argument("alntab",type=str)
parser.add_argument("output",type=str)
args = parser.parse_args()

outfile = open(args.output,'w')
for line in open(args.alntab,'r'):
    line = line.strip()
    info = line.split('\t')
    if float(info[10])>1e-4:
        continue

    outfile.write(line+'\n')

outfile.close()
