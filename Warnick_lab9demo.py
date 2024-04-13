def encode(password):
    # Encoding each digit by increasing by 3 with wrap-around using modulo 10 arithmetic
    encoded = ''
    for char in password:
        # Shift each digit up by 3, wrap around if the digit exceeds 9
        new_digit = (int(char) + 3) % 10
        encoded += str(new_digit)
    return encoded


def main():
    stored_password = ''
    while True:
        print("\nMenu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                stored_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid password. Please ensure it is an 8-digit number.")

        elif option == '2':
            if stored_password:
                print(
                    f"The encoded password is {stored_password}, and the original password is {decode(stored_password)}.")
            else:
                print("No encoded password available. Please encode a password first.")

        elif option == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()