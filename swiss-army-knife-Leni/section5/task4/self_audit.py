#!/usr/bin/env python3

import os
import psutil

process = psutil.Process(os.getpid())

start_memory = process.memory_info().rss / (1024 * 1024)
print(f"Starting Memory: {start_memory:.2f} MB")

start_cpu = process.cpu_times()

numbers = list(range(5_000_000))

end_memory = process.memory_info().rss / (1024 * 1024)
print(f"Ending Memory: {end_memory:.2f} MB")

memory_used = end_memory - start_memory
print(f"Memory Consumed: {memory_used:.2f} MB")

end_cpu = process.cpu_times()

print(f"User CPU Time: {end_cpu.user - start_cpu.user:.2f} seconds")
print(f"System CPU Time: {end_cpu.system - start_cpu.system:.2f} seconds")

# Memory Peak Observed: 203.88 MB
