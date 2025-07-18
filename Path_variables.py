# Will need this is a seperate function because I am new to using glob instead of wildcards
def find_path(pattern):# The pattern is the path to the file we are looking for
    return glob.glob(pattern)[0]# 0 is the first match. That's what we are looking for

# Path variables (absolute cinema)
CONSERVATION_PATH = find_path("/sys/bus/platform/drivers/ideapad_acpi/VPC*/conservation_mode")
FN_LOCK_PATH = find_path("/sys/bus/platform/drivers/ideapad_acpi/VPC*/fn_lock")
KBD_BACKLIGHT_PATH = find_path("/sys/bus/platform/drivers/ideapad_acpi/VPC*/leds/platform::kbd_backlight/brightness")