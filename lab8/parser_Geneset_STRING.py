# Parse the geneset to be used in STRING

print(' the output file needs minor modification.')
import sys

inFile = sys.argv[1]
outFile = sys.argv[2]

with open(inFile) as f1, open(outFile,'w') as f2:
    genes = str(f1.readlines()).replace(' ','\n')
    f2.write(genes)
