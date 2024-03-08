import secrets
import string

#A function to generate random passwords

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = '' #initialising an empty string to store random combination of passwords.
    for i in range(length):
        password += secrets.choice(characters)
    return password

def main():
    length = int(input("Enter the desired length of the password: "))#gets user input.
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
