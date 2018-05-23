import sys

setsFile = sys.argv[1]
speciesFile = sys.argv[2]

with open(setsFile) as f1, open(speciesFile) as f2:
    geneList = f2.read().splitlines() 
    print(geneList)
    maxCount = 0
    maxSet = []

    for line in f1:
        count = 0
        print(line)
        for item in line:
            #print(item)
            if item in geneList:
                print('yes')
                count = count+1
                print(count)
        if count >= maxCount:
           maxCount = count 
           #print(maxCount)
           maxSet = line

    
    #print('sss')
    for i in maxSet:
        print(i)
      

