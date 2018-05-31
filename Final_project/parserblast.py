import sys

inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile) as f:
    pairs,querys = [],[]
    hits = f.readlines()
    for lines in hits:
        pairs.append([lines.split()[0],lines.split()[1],lines.split()[10]])
        querys.append(lines.split()[0])
    
    querys = list(set(querys))
    bestHits = []
    for query in querys:
        scoreList = []
        for index, value in enumerate(pairs):
            if value[0] == query:
                scoreList.append(value[2])
        for index, value in enumerate(pairs):
            if value[0]==query and value[2]==min(scoreList):
                bestHits.append([value[0],value[1],value[2]])
            break
                
    threshold = XXXx
    
                


                
                
    
