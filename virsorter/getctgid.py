import argparse
parser = argparse.ArgumentParser()
parser.add_argument("idlist",type=str)
args = parser.parse_args()

def getid(sample,outfile):
    
    
    resfile = open('cat12/'+sample+'.12','r')
    for line in resfile:
        line = line.strip()
        info = line.split('_')
        
        ctgid = info[1]+'_'+info[2]
        leninfo = line.split('=')
        length = int(leninfo[-1].split('-')[0].split('_')[0])
        if length >=5000:
            outfile.write(ctgid+'#'+sample+'\t'+leninfo[-1]+'\n')
        elif length >=1500:
            if leninfo[-1].find('circular')<0:
                continue
            outfile.write(ctgid+'#'+sample+'\t'+leninfo[-1]+'\n')
   

def getid16(sample,outfile):
    
    resfile = open('cat16/'+sample+'.16','r')
    for line in resfile:
        line = line.strip()
        info = line.split('_')

        ctgid = info[1]+'_'+info[2]
        leninfo = line.split('=')
        length = int(leninfo[-1].split('-')[0].split('_')[0])
        if length >=5000:
            outfile.write(ctgid+'#'+sample+'\t'+leninfo[-1]+'\n')
        elif length >=1500:
            if leninfo[-1].find('circular')<0:
                continue
            outfile.write(ctgid+'#'+sample+'\t'+leninfo[-1]+'\n')
    

samples = []
for line in open(args.idlist,'r'):
    line = line.strip()
    samples.append(line)


out12 = open('virsorter.high','w')
out16 = open('virsorter.low','w')
for sample in samples:
    getid(sample,out12)
    getid16(sample,out16)

out12.close()
out16.close()
     
