#!/usr/bin/env python3

import psutil

cpu = psutil.cpu_percent(interval = 1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")

print("=" * 40)
print("		SYSTEM MONITOR")
print("=" * 40)
print(f"CPU usage: 		{cpu}%")
print(f"Available RAM: 		{memory.available /(1024**3):.2f}GB")
print(f"Disk Usage:          {disk.percent}%")
print("=" * 40)

if cpu > 80:
    print("\033[91mWARNING: CPU usage is above 80%!\033[0m")

if memory.available < 1 * 1024**3:
    print("\033[91mWARNING: Available RAM is below 1 GB!\033[0m")

if disk.percent > 80:
    print("\033[91mWARNING: Disk usage is above 80%!\033[0m")
