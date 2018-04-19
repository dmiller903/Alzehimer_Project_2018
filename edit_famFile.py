#! /usr/bin/python

import sys

#parse fam file and remove lines without case or control information

with open(sys.argv[1], "r") as readFile:
	with open(sys.argv[2], "w") as writeFile:
		for line in readFile:
			line = line.strip().split(" ")
			if "-9" in line:
					writeFile.write(line[0] + "_" + line[1] + "\n")
