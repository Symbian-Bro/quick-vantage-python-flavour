import os
import sys
import glob
import time
def root_checker():
    if os.getuid() != 0:
        print("Requesting root privileges...")
        # The following line will try executing the script with sudo (That's what she said)
        os.execvp('sudo', ['sudo', sys.executable] + sys.argv)
        sys.exit(1)

# Commented out the root checker function because the .py file itself is run with sudo (sudo python3 Quick-Vantage.py)

def find_path(pattern):# The pattern is the path to the file we are looking for
    return glob.glob(pattern)[0]# 0 is the first match. That's what we are looking for

# Path variables (Absolute cinema. The glob module will work its magic)
CONSERVATION_PATH = find_path("/sys/bus/platform/drivers/ideapad_acpi/VPC*/conservation*")
FN_LOCK_PATH = find_path("/sys/bus/platform/drivers/ideapad_acpi/VPC*/fn*")
BACKLIGHT_PATH = find_path("/sys/bus/platform/drivers/ideapad_acpi/VPC*/leds/platform::kbd_backlight/brightness")
cpu_info = find_path("/proc/cpuinfo")
temp_info = find_path("/sys/class/thermal/thermal_zone*/temp")
mem_info = find_path("/proc/meminfo")

def read_file(path):
    with open(path, 'r') as f:
            return int(f.read().strip())

def write_file(path, value):
    try:
        with open(path, 'w') as f:
            f.write(str(value))
        return True
    except Exception as e:
        print(f"Error writing to {path}: {e}")
        return False

# Conservation Mode
def toggle_conservation():
    current = read_file(CONSERVATION_PATH)
    if current is not None:
        new_value = 0 if current == 1 else 1
        if write_file(CONSERVATION_PATH, new_value):
            status = "enabled" if new_value == 1 else "disabled"
            print(f"✅ Conservation Mode {status}")

# Function Lock
def toggle_fn_lock():
    current = read_file(FN_LOCK_PATH)
    if current is not None:
        new_value = 0 if current == 1 else 1
        if write_file(FN_LOCK_PATH, new_value):
            status = "enabled" if new_value == 1 else "disabled"
            print(f"✅ Function Lock {status}")

def toggle_backlight(level):
    if level < 0 or level > 2:
        print("Invalid backlight level. Please choose between 0 and 2.")
        return
    if write_file(BACKLIGHT_PATH, level):
        print(f"✅ Keyboard Backlight set to Level {level}")
    else:
        print("❌ Failed to set Keyboard Backlight level")

# Memory info
def get_memory_stats():
    meminfo = {}
    try:
        with open('/proc/meminfo', 'r') as f:
            for line in f:
                parts = line.split(':')
                key = parts[0]
                value = parts[1].strip().split()[0]
                meminfo[key] = int(value)
        total = meminfo.get('MemTotal', 0) // 1024
        free = meminfo.get('MemAvailable', 0) // 1024
        used = total - free
        return total, used
    except Exception as e:
        print(f"Error reading memory stats: {e}")
        return 0, 0, 0

def status_n_input():
    cons = read_file(CONSERVATION_PATH)
    fn_lock = read_file(FN_LOCK_PATH)
    kbd = read_file(BACKLIGHT_PATH)
    tmp = read_file(temp_info)
    t = int(tmp/1000)
    total_mem, used_mem = get_memory_stats()

    if cons == 1:
        p = "[ ON]"
    else:
        p = "[OFF]"
    if fn_lock == 1:
        q = "[ ON]"
    else:
        q = "[OFF]"

    print("\n._______________________________.")
    print("|         Quick-Vantage         |")
    print("|===============================|")
    print("|  Current Status:              |")
    print(f"|  - Conservation Mode : {p}  |")
    print(f"|  - Function Lock     : {q}  |")
    print(f"|  - Keyboard Backlight: {kbd}      |")
    print(f"|  - System Temperature: {t}°C   |")
    print("|-------------------------------|")
    print("|         Memory Usage          |")
    print("|-------------------------------|")
    print(f"|Used : {used_mem}MB | Total : {total_mem}MB|")
    print("|===============================|")
    print("|  Options:                     |")
    print("|  1) Toggle Conservation Mode  |")
    print("|  2) Toggle Function Lock      |")
    print("|  3) Set Keyboard Backlight    |")
    print("|  4) View CPU Information      |")
    print("|  q) Quit                      |")
    print("|_______________________________|")
    print("\n")  # Just a new line

def main():
    root_checker()

    while True:
        status_n_input()
        choice = input("Choose an option (1-4, q): ").lower()

        if choice == '1':
            toggle_conservation()
        elif choice == '2':
            toggle_fn_lock()
        elif choice == '3':
                level = int(input("Enter backlight level (0-2): "))
                toggle_backlight(level)
        elif choice == '4':
            with open("/proc/cpuinfo", "r") as f:
                 for line in f:
                     if "model name" in line:
                         print(line.split(":", 1)[1].strip())
                         break
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again")
        time.sleep(1)

if __name__ == "__main__":
    main()