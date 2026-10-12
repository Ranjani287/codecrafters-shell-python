import shutil
import sys
import subprocess

def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        input_command = input()
        cmd=input_command[5:]
        if input_command.__contains__("type") and cmd in ["type", "echo", "exit"]:
            print(cmd+" is a shell builtin")
        elif path := shutil.which(cmd):
             subprocess.run(input_command.split())
        elif input_command == "exit":
            break
        elif input_command.__contains__("echo"):
            print(input_command[5:])
        else:
         if input_command.__contains__("type"):
            print(input_command[5:] + ": not found")
         else:        
            print(input_command + ": not found")



if __name__ == "__main__":
    main()
