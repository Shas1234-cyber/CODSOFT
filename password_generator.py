import random
import string

def generate_password(length, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation if use_symbols else ''

    all_characters = lower + upper + digits + symbols

    if not all_characters:
        print("Error: No character types selected.")
        return ""

    # Ensure password has at least one of each required character type
    password = []
    password.append(random.choice(lower))
    password.append(random.choice(upper))
    password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    # Add random characters to reach desired length
    while len(password) < length:
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return ''.join(password)

def show_menu():
    print("\n==============================")
    print("      PASSWORD GENERATOR")
    print("==============================")
    print("1. Generate Strong Password (with symbols)")
    print("2. Generate Medium Password (no symbols)")
    print("3. Exit")

def main():
    print("Welcome to the Password Generator!")

    while True:
        show_menu()
        choice = input("\nSelect an option (1-3): ")

        if choice == '1' or choice == '2':
            try:
                length = int(input("Enter desired password length (minimum 6): "))
                if length < 6:
                    print("Password length should be at least 6 characters for better security.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            use_symbols = True if choice == '1' else False
            password = generate_password(length, use_symbols)
            print(f"\nYour generated password: {password}")
        elif choice == '3':
            print("\nThank you for using the Password Generator. Stay safe!")
            break
        else:
            print("Invalid choice! Please select from the menu.")

        again = input("\nDo you want to generate another password? (y/n): ").lower()
        if again != 'y':
            print("\nGoodbye! Stay secure.")
            break

if __name__ == "__main__":
    main()
