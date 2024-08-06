# Adding the password
def add_password():
  while True:
      website = input("Enter the website name: ").strip()
      username = input("Enter the username: ").strip()
      password = input("Enter the password: ").strip()

      if website == "" or username == "" or password == "":
          print("All fields are required. Please try again!")
      else:
          # Open the file in append mode and write the data
          try:
              with open("passwords.txt", "a") as file:
                  file.write(f"WEBSITE NAME: {website} | USER NAME: {username} | PASSWORD: {password}\n")
              print("Password added successfully!")
          except IOError:
              print("An error occurred while saving the password.")

      review = input("Cntinue to add passwords? (yes/no): ").lower().strip()
      if review.lower() == "yes":
          add_password()
      else:
          a = input("Do you want to see your passwords? (yes/no): ").strip().lower()
          if a.lower() == "yes":
                view_passwords()
          else:
                print("Okay.")
          break

# Viewing the passwords
def view_passwords():
  # Open the file in read mode and read the data
  try:
      with open("passwords.txt" , "r") as file:
          passwords = file.read()
          if passwords:
              print("Stored Passwords:")
              print(passwords)
          else:
              print("No passwords stored yet.")
  except FileNotFoundError:
      print("No passwords stored yet.")

add_password()