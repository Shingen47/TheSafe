import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def hash_password(self, password):
        # Use SHA-256 for hashing (you can choose a more secure algorithm if needed)
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def add_password(self, website, username, password):
        hashed_password = self.hash_password(password)
        if website not in self.passwords:
            self.passwords[website] = {'username': username, 'password': hashed_password}
            print("Password added successfully!")
        else:
            print("Website already exists. Use update_password() to modify the password.")

    def retrieve_password(self, website):
        if website in self.passwords:
            username = self.passwords[website]['username']
            password = self.passwords[website]['password']
            print(f"Website: {website}\nUsername: {username}\nPassword: {password}")
        else:
            print("Website not found in the password manager.")

    def update_password(self, website, new_password):
        if website in self.passwords:
            self.passwords[website]['password'] = self.hash_password(new_password)
            print("Password updated successfully!")
        else:
            print("Website not found in the password manager.")

def main():
    safe = PasswordManager()

    while True:
        print("\nWelcome to The Safe - Password Manager")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. Update Password")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            safe.add_password(website, username, password)
        elif choice == '2':
            website = input("Enter website: ")
            safe.retrieve_password(website)
        elif choice == '3':
            website = input("Enter website: ")
            new_password = input("Enter new password: ")
            safe.update_password(website, new_password)
        elif choice == '4':
            print("Exiting The Safe. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
