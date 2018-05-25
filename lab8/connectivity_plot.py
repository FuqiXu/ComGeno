import re
import glob
import matplotlib.pyplot as plt

def links(inFile):
    interNum = 0 
    with open(inFile,'r') as f:
        uniqueGenes = set()
        allGenes = []
        allInter = []
    
        for line in f:
            gene = re.match(r'\d+.(\w+)',line)
            # Storing all interactions
            allGenes.append(gene.group(1))
    
            # Storing the unique proteins
            uniqueGenes.add(gene.group(1))
    
            # Count how many lines to calculate average connectivity
            if line !='\n':
                interNum = interNum + 1
        
        # Calculating the average connectivity
        geneNum = len(uniqueGenes)
        averConnect = interNum/geneNum
        print(averConnect)
    
        # For each protein, count the iteractions it has.
        for i in uniqueGenes:
            perInter= allGenes.count(i)
            allInter.append(perInter)
    
        # Count the frequency of one node degree appears
        allFreq = []
        # The x-axis
        nodes = list(set(allInter))
        # The y-axis
        for i in nodes:
            frequency = allInter.count(i) 
            allFreq.append(frequency)
    return nodes,allFreq,averConnect

filenames = glob.glob('geno?')
for i in range(len(filenames)):
    node,link,aver = links(filenames[i])
    plt.scatter(node,link)
    #plt.autoscale()
    plt.xscale('log')
    plt.yscale('log')
    plt.axvline(x=aver,color='k', linestyle='--',label='average connectivity')
    plt.title('geno'+str(i+1))
    plt.xlabel('node degree')
    plt.ylabel('frequency')
    plt.savefig('geno'+str(i+1)+'.png')
    plt.show()
    

