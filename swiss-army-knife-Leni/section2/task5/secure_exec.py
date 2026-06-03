#!/usr/bin/env python3

import subprocess

def unsafe_run(user_input):
	subprocess.run(f"echo {user_input}", shell = True)

#insecure example ^^
#shell = True causes the string to be interpreted by the command line/shell.
#an attacker could put commands into this input and they would then be ran


def safe_run(user_input):
	subprocess.run(["echo", user_input])

#secure example ^^
#Both the command and the user input is passed as a list this causes
#each one to be treated like data rather than being interpreted by the shell

if __name__ == "__main__":
	test_input = "Hello World"

	print("Unsafe")
	unsafe_run(test_input)

	print("Safe")
	safe_run(test_input)

