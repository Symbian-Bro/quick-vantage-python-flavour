def status():
    cons = read_file(CONSERVATION_PATH)
    fn_lock = read_file(FN_LOCK_PATH)
    kbd_backlight = read_file(KBD_BACKLIGHT_PATH)

    if cons == "1":
        p = [ ON]
    else:
        p = [ OFF]
    if fn_lock == "1":
        q = [ ON]
    else:
        q = [ OFF]

    print("\n._______________________________.")
    print("|         Quick-Vantage         |")
    print("|===============================|")
    print("|  Current Status:              |")
    fprint(f"|  - Conservation Mode: {p}      |")
    print(f"|  - Function Lock:     {q}      |")
    print("|===============================|")
    print("|  Options:                     |")
    print("|  1) Toggle Conservation Mode  |")
    print("|  2) Toggle Function Lock      |")
    print("|  q) Quit                      |")
    print("|_______________________________|")
