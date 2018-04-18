#Filter .fam file from PLINK to include a file with only CASES, excluding
#controls. A new file is created with only CASES.

#This script accepts 3 arguments: 1) the name of the .py file, 2) the path
#to the PLINK .fam file, 3) the name of the output file.

from sys import argv

path = argv[1]
output = argv[2]

with open(path) as dataFile, open(output, 'w') as outputFile:
    import re
    for line in dataFile:
        lineCheck = line.split(" ")
        if "2" in lineCheck[5]:
            outputFile.write(lineCheck[0] + "_" + lineCheck[1] + "\n")
            
