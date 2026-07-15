#!/usr/bin/env python3

import json

filename = "config.json"

try:
	with open(filename, "r") as file:
		config = json.load(file)

	config["status"] = "maintenance"

	with open(filename, "w") as file:
		json.dump(config, file, indent = 4)

	print("Configuration updated successfully.")

except FileNotFoundError:
	print(f"Error: '{filename}' was not found.")

except PermissionError:
	print(f"Error: Permission denied when accessing '{filename}.")

except Exception as e:
	print(f"An unexpected error occurred: {e}")

finally:
	print("Operation Attempted")
