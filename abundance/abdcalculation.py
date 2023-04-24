import pandas as pd

ctgdata = []
samples = []
data = []
numdata = []
sp2rpkm = {}
detaildata = []
for filename in os.listdir('ctgrpkm'):
    sample = filename.split('.')[0]
    samples.append(sample)
    sampledata = {}
    samplenum = {}
    detail = {}
    df = pd.read_csv('ctgrpkm/'+filename,sep='\t',header=None)
    df.columns = ['ctg','rpkm']

    for ctg,rpkm in zip(df['ctg'],df['rpkm']):
        ctgid = ctg+'#'+sample
        if not ctgid in ctg2sp.keys():
            continue
        if not ctgid in validset:
            continue
        #taxid = ctg2tax[ctgid]
        sp = ctg2sp[ctgid]
        #ctg_after_filter.append([ctgid,taxid,sp])

        if sp in sp2rpkm.keys():
            sp2rpkm[sp].append(rpkm)
        else:
            sp2rpkm[sp] = [rpkm]
        if sp in sampledata.keys():
            sampledata[sp] += rpkm
            samplenum[sp] += 1
            detail[sp].append(rpkm)

        else:
            sampledata[sp] = rpkm
            samplenum[sp] = 1
            detail[sp] = [rpkm]

    #for sp in sampledata.keys():
        #sampledata[sp]/=samplenum[sp]
    data.append(sampledata)
    numdata.append(samplenum)

    detaildata.append(detail)

N = len(samples)
datam = {}
numlist = []
for sp in splist:
    datam[sp] = []
for i in range(N):
    sample = samples[i]
    sample2data = data[i]

    for sp in splist:
        num = 0
        if sp in sample2data.keys():
            num = sample2data[sp]
            if num > 0 and num<5:
                numlist.append(num)
            if num<0.5:
                num = 0

        datam[sp].append(num)
df = pd.DataFrame(datam,index=samples)
df.to_csv('abundance.csv',sep='\t',index=True)
