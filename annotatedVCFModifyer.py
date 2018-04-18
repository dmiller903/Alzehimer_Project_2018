#This script removes the body of the annotated VCF file. It also changes
#patient genotype for machine learning, example:

#0/0 -> 0
#1/0 -> 1
#0/1 -> 1
#1/1 -> 2

#This script accepts 3 arguments, 1) the name of the .py file,
#2) the input .vcf file, 3) the output file (recommended .tsv).

from sys import argv
path = argv[1]
output = argv[2]
with open(path) as dataFile, open(output, 'w') as outputFile:
    for line in dataFile:
        if "##" in line:
            continue
        line = line.replace("#CHROM", "CHROM")
        line = line.replace("0/0", "0")
        line = line.replace("1/0", "1")
        line = line.replace("0/1", "1")
        line = line.replace("1/1", "2")
        outputFile.write(line)
