# -*- coding: utf-8 -*-
"""
This file searches for the shared sequence in all genomes

and returns multiple files, each containing one ortholog in all genomes in FASTA format

"""
import sys

blastresult = sys.argv [1]
'''
with open("all_clusters",'a+') as g:
		

with open(blastresult) as f1: 
    g = open(blastreslt+'cluster','a+')
    for i in g
    g.write(hits1[i][0]+' '+hits1[i][2]) 
'''  
      
with open(blastresult) as f:
    lines = f.readlines()
    orth = []
    for x in lines:
        orth.append(x.split(' '))
with open(blastresult+'geneID','w+') as g:
    for i in orth:
        g.write(i[0]+' '+i[2]+'\n')



		
    
