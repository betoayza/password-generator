import secrets

print("\nWellcome to Password Generator 2023!")


def format_new_password(password):
    new_password = ""
    list_chars = []

    # Extract chars
    i = 0
    while i < len(password):
        if password[i].isalpha():
            if len(list_chars) > 0 and list_chars[-1].islower():
                list_chars.append(password[i].upper())
            else:
                list_chars.append(password[i])
        i += 1

    # Update password
    j = 0
    for i in range(0, len(password)):
        if password[i].isalpha():
            while j < len(list_chars):
                new_char = list_chars[j]
                new_password += new_char
                j += 1
                break
        else:
            new_password += password[i]
    return new_password


is_running = True
while is_running:
    try:
        option = int(input("""\nPassword length: 
        1. 8
        2. 10
        3. 12
        4. 16
        Choose: """))

        # 16 bytes = 16 * 8 bits = 128 bits => 128 bits / 4 = 32 hexa digits
        new_password = secrets.token_hex(16)

        if option == 1:
            new_password = new_password[:8]

        elif option == 2:
            new_password = new_password[:10]

        elif option == 3:
            new_password = new_password[:12]

        elif option == 4:
            new_password = new_password[:16]

        else:
            print("\nInvalid option!")
            continue

        # alternate lowers and capitalizeds
        new_password = format_new_password(new_password)

        print("\nSuccessful! New password is:", new_password)
        is_running = False

    except:
        print("\nThat's not a number, ha!")

print("\nThank for try me! See on")
