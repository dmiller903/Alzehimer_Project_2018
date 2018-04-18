#This script adds either CASE or CONTROL to the second column
# of a tidy output file from the R function 'makeAnnotatedVcfTidy'.
#The classPath file was created with the script 'filterFam.py' 
#using the .fam output file from PLINK. 

#This script accepts 4 arguments, 1) the name of the .py file,
#2) the tidy input .tsv file, 3) the output file (recommended .tsv),
#4) the file containing all the 'CASE' names.

from sys import argv
inputFile = argv[1]
outputPath = argv[2]
classPath = argv[3]

with open(inputFile) as dataFile, open(classPath) as classFile, open(outputPath, 'w') as writeFile:
    lineCount = 0
    newList = []
    for line in classFile:
        line = line.strip("\n")
        newList.append(line)
    for line in dataFile:
        lineCount += 1
        if lineCount == 1:
            line = line.split("\t")
            line.insert(1, "Class")
            line = "\t".join(line)
            writeFile.write(line)
        else:
            line = line.split("\t")
            if line[0] in newList:
                line.insert(1, "CASE")
                line = "\t".join(line)
                writeFile.write(line)
            else:
                line.insert(1, "CONTROL")
                line = "\t".join(line)
                writeFile.write(line)
