#usr/bin/env python3

def read_log (filename):
	with open(filename, "r") as file:
		for line in file:
			yield line

keyword = "CRITICAL"

for line in read_log("sample.log"):
	if keyword in line:
		print(line.strip())
