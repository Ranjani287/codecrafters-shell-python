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
        if args[1] in ["exit", "echo", "type", "pwd", "cd"]:
            print(f"{args[1]} is a shell builtin")
        elif path := shutil.which(args[1]):
            print(f"{args[1]} is {path}")
        else:
            print(f"{args[1]}: not found")

    elif cmd == "echo":
        print(" ".join(args[1:]))

    elif cmd == "pwd":
        print(os.getcwd())

    elif cmd == "cd":
        try:
            path= args[1]
            if path == "~":
                os.chdir(os.environ.get("HOME"))
            if path:
                os.chdir(path)
            else:
                print("cd: HOME not set")

        except IndexError:
            print("cd: missing directory")
        except OSError:
            print(f"cd: {args[1]}: No such file or directory")

    elif path := shutil.which(cmd):
            subprocess.run(args)

    else:
        print(f"{cmd}: command not found")