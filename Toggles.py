def write_file(path, value):
    try:
        with open(path, 'w') as f:
            f.write(str(value))
        return True

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