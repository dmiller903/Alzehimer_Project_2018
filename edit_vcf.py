#This script calulates the the number of genotypes and then generates a new file based on set conditions
#The conditions can be modified to generate different output files

#This script accepts 3 arguments
#1) the input vcf file
#2) the name of the output vcf file to be created
#3) a second output file with details on the number of different genotypes

#! /usr/bin/python

import sys

with open(sys.argv[1], "r") as readFile:
	with open(sys.argv[2], "w") as writeFile:
		with open(sys.argv[3], "w") as writeCount:
			writeCount.write("POS" + "\t" + "ID" + "\t" + "NUM_A" + "\t" + "NUM_B" + "\t" + "NUM_C" + "\t" + "NUM_D" + "\t" + "NUM_E" + "\t" + "NUM_F" + "\n")
			for line in readFile:
				if line[0] == "#":
					writeFile.write(line)
				else:
					line = line.strip().split("\t")
					a = line.count("./.")
					b = line.count("0/0")
					c = line.count("0/1")
					d = line.count("1/0")
					e = line.count("1/1")
					f = b + c + d + e
					g = a + b + c + d + e
					writeCount.write(line[1] + "\t" + line[2] + "\t" + str(a) + "\t" + str(b) + "\t" + str(c) + "\t" + str(d) + "\t" + str(e) + "\t" + str(f) + "\t" + str((f/g)) + ("\n))
					if (f/g) > 0.5:
						writeFile.write(line + "\n")
