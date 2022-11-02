#!/usr/bin/python3

import sys

sys.stdout = open(sys.argv[2], 'w')

genre = list()
result = {}

with open(sys.argv[1]) as f:
	for line in f:
		data = line.strip().split('::')
		genres = data[2].split('|')
		for g in genres:
			if g in result.keys():
				result[g] += 1
			else:
				result[g] = 1
for k, v in result.items():
	print("{} {}".format(k,v))
sys.stdout.close()

