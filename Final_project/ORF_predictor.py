import sys

inGeno = sys.argv[1]

with open(inGeno) as f1:
    geno = f1.readlines()[1]

    # Check input file
    nuc = ['A','T','G','C']
    for i in geno:
        if i not in nuc:
            print(i)
            sys.exit("Wrong Input")


    # Read the genome in six reading frames
    allCodons = []
    for k in [0,1,2]:
        codons = []
        for i in range(k,len(geno)-2-k):
            codons.append(geno[i]+geno[i+1]+geno[i+2])
        allCodons.append(codons)

    geno_rev = geno[::-1]
    for k in [0,1,2]:
        codons = []
        for i in range(k,len(geno)-2-k):
            codons.append(geno_rev[i]+geno_rev[i+1]+geno_rev[i+2])
        allCodons.append(codons)

    ## Assumpution 1: start and stop codons
    start = ['TAC']
    stop = ['ATT','ACT','ATC']
    genes = []
    for i in range(len(allCodons)):
        for j in range(len(allCodons)):
            if allCodons[i][j] in start:
                gene = ''

                '''
                for j allCodons[i][j] not in stop:
                    print(allCodons[i][j])
                    gene = gene + allCodons[i][j]
                    print(gene)
                    j = j+1
                #gene = gene + allCodons[i][j]

                genes.append(gene)

    print(len(genes))
    for i in range(len(genes)):
        print(genes[i])
        print(len(genes[i]))
      '''
