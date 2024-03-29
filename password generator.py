import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters from the set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    try:
        # Prompt the user for the desired password length
        length = int(input("Enter the desired password length: "))

        # Generate the password
        password = generate_password(length)

        # Display the generated password
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid positive integer for the password length.")

if __name__ == "__main__":
    main()
