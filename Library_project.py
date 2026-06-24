def main():
    print("--welcome to Library system--")

def register_user():
    # Note: Added a prompt reminder to type a space between name and password
    name, password = input("Enter your name and password (separated by a space): ").split()
    return [name,password]

# Call main once at the start
main()

library_files = ["DataScience_intro.pdf", "CyberSecurity_basics.pdf", "Linux_guide.md", "AccountingBasics.pdf"]
registered_users = []

while True:
    print("\n1. Register")
    print("2. Login & Access files")
    print("3. Exit")

    choice = input("Choose an option: ")
    
    if choice == "1":
        new_user = register_user()
        registered_users.append(new_user)
        print(f"Registration successful for: {new_user}")

    elif choice == "2":
        # Placeholder for your login logic
        print("\n --Login---")
        login_name =input("enter your username")
        login_pass =input("enter your password :")
        access_granted = False
        for user in registered_users:
            if user[0] == login_name and user[1]==login_pass:
                access_granted=True
                break
        if access_granted:
            print("\n Login Sucessfull! Accessing Librru Files...")
            for file in library_files:
                print(f"- {file}")
        else:
            print("\n Invalid Username or password . Please Register First.")

    elif choice == "3":
        print("Goodbye!")
        break  # This actually stops the while loop
        
    else:
        print("Invalid choice. Please select 1, 2, or 3.")