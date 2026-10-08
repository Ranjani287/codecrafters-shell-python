import sys


def main():
    # TODO: Uncomment the code below to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        input_command = input()
        if input_command == "exit":
            break
        print(input_command + ": command not found")



if __name__ == "__main__":
    main()
