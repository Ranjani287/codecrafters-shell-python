import os
import sys
import shutil
import subprocess

while True:
    command = input("$ ")

    if not command:
        continue

    args = command.split()
    cmd = args[0]

    if cmd == "exit":
        break

    elif cmd == "type":
        if args[1] in ["exit", "echo", "type"]:
            print(f"{args[1]} is a shell builtin")
        elif path := shutil.which(args[1]):
            print(f"{args[1]} is {path}")
        else:
            print(f"{args[1]}: not found")

    elif cmd == "echo":
        print(" ".join(args[1:]))

    elif cmd == "cd":
        try:
            os.chdir(args[1])
        except (IndexError, FileNotFoundError):
            print(f"cd: {args[1] if len(args) > 1 else ''}: No such file or directory")

    elif path := shutil.which(cmd):
        subprocess.run(args)

    else:
        print(f"{cmd}: command not found")