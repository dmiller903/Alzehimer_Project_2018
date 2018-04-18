#! /usr/bin/python

import sys

with open(sys.argv[1], "r") as readFile:
	with open(sys.argv[2], "w") as writeFile:
		with open(sys.argv[3], "w") as writeCount:
			for line in readFile:
				if line[0] == "#":
					writeFile.write(line)
				else:
					a = line.count("./.")
					b = line.count("0/0")
					c = line.count("0/1")
					d = line.count("1/0")
					e = line.count("1/1")
					f = b + c + d + e
					g = a + b + c + d + e
					if (f/g) > 0.5:
						writeFile.write(line)
					if (f/g) > 0.5:
						writeCount.write(str(a) + "\t" + str(b) + "\t" + str(c) + "\t" + str(d) + "\t" + str(e) + "\t" + str(f) + "\t" + str((f/g)) + ("\n"))
