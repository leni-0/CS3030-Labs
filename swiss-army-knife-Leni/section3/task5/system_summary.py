#!/usr/bin/env python3

import subprocess
import re

result = subprocess.run(
	["who"],
	capture_output = True,
	text = True
)

pattern = r"(\S+)\s+(\S+)\s+(\d{4}-\d{2}-\d{2}|\w{3}\s+\d+)\s+(\d{2}:\d{2})"

matches = re.findall(pattern, result.stdout)

print("=" * 60)
print(f"{'User':<15}{'Terminal':<15}{'Date':<15}{'Time':<10}")
print("=" * 60)

for user, terminal, date, time in matches:
	print(f"{user:<15}{terminal:<15}{date:<15}{time:<10}")

print("=" * 60)
