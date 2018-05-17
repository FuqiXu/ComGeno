import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

def reader(f):
    lines = f.readlines()
    orth = []
    for x in lines:
        orth.append(x.split(' '))
    return orth

with open(file1,'r') as f1, open(file2,'r') as f2,open(file3,'r') as f3:
    orth1 = reader(f1)
    orth2 = reader(f2)
    orth3 = reader(f3)

clusters = {}

for item in orth1:
    item[1] = item[1].replace('\n','')
    clusters[item[0]] = item[1]

for item in orth2:
    if item[0] not in clusters:
        item[1] = item[1].replace('\n','')
        clusters[item[0]] = item[1]
    else: 
        item[1] = item[1].replace('\n','')
        clusters[item[0]] = clusters[item[0]]+' '+item[1]

for item in orth3:
    if item[0] not in clusters:
        item[1] = item[1].replace('\n','')
        clusters[item[0]] = item[1]
    else: 
        item[1] = item[1].replace('\n','')
        clusters[item[0]] = clusters[item[0]]+' '+item[1]
    
with open("allClusters",'a+') as g:
    for key in clusters:
        g.write(key)
        g.write(' '+clusters[key])
        g.write('\n')

