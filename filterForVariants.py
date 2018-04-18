#This script will filter an output .vcf file from PLINK to include
#'HIGH' variants or 'HIGH' and 'MODERATE' variants by excluding the
#comment in the script. This script also removes the vcf header.

#This script accepts 3 arguments: 1) The name of the .py script, 2)
#the name of the input .vcf file, 3) the name of the output file.

from sys import argv

inputFile = argv[1]
outputFile = argv[2]

with open(inputFile) as dataFile, open(outputFile, 'w') as output:
    for line in dataFile:
        if "##" in line:
            continue
        if "#" in line:
            output.write(line)
        if "HIGH" in line: #or "MODERATE" in line:
            output.write(line)
