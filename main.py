def main():
    root_checker_boy()

    while True:
        status()
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
        time.sleep(1) # Sleep

if __name__ == "__main__":
    main()