#!/usr/bin/env python3

import re

with open("sample.log", "r") as file:
	log_data = file.read()

ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
timestamp_pattern = r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}\]"

ips = re.findall(ip_pattern, log_data)
timestamps = re.findall(timestamp_pattern, log_data)

print("IP addresses:")
for ip in ips:
	print(ip)

print ("\nTimestamps:")
for timestamp in timestamps:
	print(timestamp)
