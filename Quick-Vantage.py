import os
import sys
import glob
import time
def root_checker_boy():
    if os.getuid() != 0:
        print("Requesting root privileges...")
        #The following line will try executing the script with sudo (That's what she said)
        os.execvp('sudo', ['sudo', sys.executable] + sys.argv)
        sys.exit(1)

def find_path(pattern):# The pattern is the path to the file we are looking for
    return glob.glob(pattern)[0]# 0 is the first match. That's what we are looking for

# Path variables (Absolute cinema. The glob module will work its magic)
CONSERVATION_PATH = find_path("/sys/bus/platform/drivers/ideapad_acpi/VPC*/conservation*")
FN_LOCK_PATH = find_path("/sys/bus/platform/drivers/ideapad_acpi/VPC*/fn*")

def read_file(path):
    with open(path, 'r') as f:
            return int(f.read().strip())

def status_n_input():
    cons = read_file(CONSERVATION_PATH)
    fn_lock = read_file(FN_LOCK_PATH)

    if cons == "1":
        p = "[ ON]"
    else:
        p = "[ OFF]"
    if fn_lock == "1":
        q = "[ ON]"
    else:
        q = "[ OFF]"

    print("\n._______________________________.")
    print("|         Quick-Vantage         |")
    print("|===============================|")
    print("|  Current Status:              |")
    print(f"|  - Conservation Mode: {p}      |")
    print(f"|  - Function Lock:     {q}      |")
    print("|===============================|")
    print("|  Options:                     |")
    print("|  1) Toggle Conservation Mode  |")
    print("|  2) Toggle Function Lock      |")
    print("|  q) Quit                      |")
    print("|_______________________________|")
    print("\n")  # Just a new line

def main():
    root_checker_boy()

    while True:
        status_n_input()
        choice = input("\nChoose an option (1-3, q): ").lower()

        if choice == '1':
            toggle_conservation()
        elif choice == '2':
            toggle_fn_lock()
        elif choice == 'q':
            print("Goodbye!")
            break # See ya later
        else:
            print("Invalid option, please try again")
        time.sleep(1)  # I'll be back soon

if __name__ == "__main__":
    main()