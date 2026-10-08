import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        input_command = input()
        if input_command.__contains__("type") and (input_command.__contains__("echo") or input_command.__contains__("exit") or input_command.__contains__("type type")):
            print(input_command[5:]+" is a shell builtin")
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
