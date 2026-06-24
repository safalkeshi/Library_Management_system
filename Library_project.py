def main():
   print("--welcome to Library system--")

def register_user():
 name, password=input("enter Your name and password( enter space button ): ").split()
 return name
main()




library_files =["DataScience_intro.pdf","CyberSecurity_basics.pdf","Linux_guide.md","AccountingBasics.pdf"]
registered_users=[]


while True:
    print("\n1. Register")
    print("2. Login & Access files")
    print("3. Exit")

    choice =input("choose an option: ")
    if choice =="1" :
      new_user = register_user()
    registered_users.append(new_user)
    print(f"Registration successful for: {new_user}")

else :
   print("goodbye")
   

