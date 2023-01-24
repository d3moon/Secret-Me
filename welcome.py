def secret_me():
    print("   ▄▄▄▄▄   ▄███▄   ▄█▄    █▄▄▄▄ ▄███▄     ▄▄▄▄▀     █▀▄▀█ ▄███▄  ")
    print("  █     ▀▄ █▀   ▀  █▀ ▀▄  █  ▄▀ █▀   ▀ ▀▀▀ █        █ █ █ █▀   ▀ ")
    print("▄  ▀▀▀▀▄   ██▄▄    █   ▀  █▀▀▌  ██▄▄       █        █ ▄ █ ██▄▄   ")
    print(" ▀▄▄▄▄▀    █▄   ▄▀ █▄  ▄▀ █  █  █▄   ▄▀   █         █   █ █▄   ▄▀")
    print("           ▀███▀   ▀███▀    █   ▀███▀    ▀             █  ▀███▀  ")

    choice = input("Do you want to continue? (y/n): ")
    if choice.lower() in ['yes', 'y']:
        print("Access granted.")
        password = input('Insert the password: ')
        import main
        main.obfuscate_payload(password)
        return None
    else:
        print("Access denied.")

secret_me()

