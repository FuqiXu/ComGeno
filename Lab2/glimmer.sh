tigr-glimmer long-orfs -n -t 1.15 51.fa.txt 51.long-orf-coords
tigr-glimmer extract -t 51.fa.txt 51.long-orf-coords > 51.longorf
tigr-glimmer build-icm -r 51.icm < 51.longorf
tigr-glimmer glimmer3 -o50 -g110 -t30 51.fa.txt 51.icm 51.glimmer

