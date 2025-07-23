password = "" # Initialize an empty password variable

# Keep asking for password while it's not correct

while password != "Admin123": #Keep looping until the correct password is entered
    
    password = input("\nEnter your password: ") # Ask user for password
    
    if password != "Admin123": # If they got it wrong
        
        print("Incorrect password, are you sure you're not a hacker? Try again.") # Tell them it's wrong and to try again
        attempts = 0
        while password != "Admin123" and attempts < 3:
            password = input("\nEnter your password: ")
            attempts += 1
        if attempts == 3:
            print("Too many attempts! Access denied.")
            break
    else:
        print("Access granted! Welcome to the system.") # This will print when the correct password is entered   
          
print("_" * 40)
