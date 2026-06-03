shell = True should be avoided, especially when there is a possibility you won't
be able to trust the user input. If the script uses shell = True it allows for a 
hacker to inject commands, that would then be interpreted and ran by the shell.
Instead user input should be passed as a list of data. This avoids the use of 
shell = True.
