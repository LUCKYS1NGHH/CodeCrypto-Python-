import random, string, os

#helper functions for encryption and decryption
def encrypt_message(plain_text, key):
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    cipher_text = ""
    for letter in plain_text:
        if letter in chars:
            index = chars.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter  #leave unsupported characters unchanged..
    return cipher_text

def decrypt_message(cipher_text, key):
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += chars[index]
        else:
            plain_text += letter  # Leave unsupported characters unchanged
    return plain_text

def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def save_message_to_file(filename, message, encrypted=False, key=None):
    folder_path = "messages"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    with open(os.path.join(folder_path, filename), "w") as f:
        f.write("Encrypted: " + str(encrypted) + "\n")
        if encrypted and key:
            message = encrypt_message(message, key)
        f.write("Message: " + message + "\n")
    print(f"Message saved to {filename}")

def decrypt_file_message(filename, key):
    folder_path = "messages"
    file_path = os.path.join(folder_path, filename)

    if not os.path.exists(file_path):
        print("File not found. Please check the filename.")
        return

    with open(file_path, "r") as f:
        lines = f.readlines()

    # Ensure file format is correct
    if len(lines) < 2 or not lines[0].startswith("Encrypted:") or not lines[1].startswith("Message:"):
        print("Invalid file format. Cannot decrypt.")
        return

    encrypted = lines[0].strip().split(": ")[1] == "True"
    message = lines[1].strip().split(": ", 1)[1]

    if encrypted:
        decrypted_message = decrypt_message(message, key)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("The message is not encrypted. Content:")
        print(message)

# Main program with options
def main():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)

    while True:
        print("\n-=| CODE CRYPTO |=-")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Generate a random password")
        print("4. Save encrypted message to a txt file")
        print("5. Decrypt a message from a txt file")
        print("6. What is this?")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            plain_text = input("Enter a message to encrypt: ")
            cipher_text = encrypt_message(plain_text, key)
            print(f"Original message: {plain_text}")
            print(f"Encrypted message: {cipher_text}")

        elif choice == "2":
            cipher_text = input("Enter a message to decrypt: ")
            plain_text = decrypt_message(cipher_text, key)
            print(f"Encrypted message: {cipher_text}")
            print(f"Original message: {plain_text}")

        elif choice == "3":
            length = int(input("Enter the length of the password: "))
            password = generate_random_password(length)
            print(f"Generated password: {password}")

        elif choice == "4":
            filename = input("Enter the filename to save the encrypted message (e.g., message.txt): ")
            message = input("Enter the message to save: ")
            save_option = input("Do you want to encrypt the message before saving? (y/n): ").strip().lower()
            encrypted = True if save_option == "y" else False
            save_message_to_file(filename, message, encrypted, key if encrypted else None)

        elif choice == "5":
            filename = input("Enter the filename to decrypt the message (e.g., message.txt): ")
            decrypt_file_message(filename, key)

        elif choice == "7":
            print("Exiting CodeCrypto...")
            break

        elif choice == "6":
            print("CodeCrypto is a python script that encrypts/decrypts messages, it's dynamic it means you can encrypt/decrypt message for only 1 session or you can say its temporary to encrypt a message. This script not uses any third party libraries like cryptography or else.")

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
