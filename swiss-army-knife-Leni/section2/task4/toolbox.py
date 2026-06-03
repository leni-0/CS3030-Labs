#!/usr/bin/env python3

import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
	description = "Recursively search for files by their exetension."
)

parser.add_argument(
	"--path",
	required = True,
	help = "Directory path to scan"
)

parser.add_argument(
	"--ext",
	required = True,
	help = "File extension to search for ex. .txt, .py, .tmp"
)

args = parser.parse_args()

for file in Path(args.path).rglob(f"*{args.ext}"):
	print(f"Found: {file}")

