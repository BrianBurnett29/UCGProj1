#EXAMPLE 1: COUNTING UP
# Start with count variable
count = 1 # This is the starting number

# This while loop checks if count is less than or equal to 5
while count <= 5:
    print(f"Count is: {count}") # Prints the current value of count
    count = count + 1 # IMPORTANT: Increments count by 1 each time the loop runs
    
print("Loop finished! Count is now:", count) # This will print after the loop is done
print("_" * 40)

#EXAMPLE 2: COUNTDOWN
# Start countdown from 10
countdown = 10 # This is the starting number for countdown

#Keep looping until countdown reaches 0
while countdown > 0:
    print(f"Countdown: {countdown}") # Prints the current countdown value
    countdown -= 1 # Decrease countdown by 1 each time the loop runs
    
print("🚀 Blast off!") # This will print after the countdown reaches 0
print("_" * 40)

#EXAMPLE 3: USING WHILE LOOP FOR USER INPUT
password = "" # Initialize an empty password variable

# Keep asking for password while it's not correct
while password != "Admin123": #Keep looping until the correct password is entered
    password = input("\nEnter your password: ") # Ask user for password
    if password != "Admin123": # If they got it wrong
        print("Incorrect password, are you sure you're not a hacker? Try again.") # Tell them it's wrong and to try again
    else:
        print("Access granted! Welcome to the system.") # This will print when the correct password is entered
print("_" * 40)
 

#EXAMPLE 4: Adding Numbers Until User Decides to Stop
total = 0 # This variable will hold the total sum of numbers entered by the user
number = 1 # Start with a number that is not 0 to enter the loop

print("Enter numbers to add up. Enter 0 to stop.")

# Keep looping until the user enters 0
while number != 0:
    number = int(input("Enter a number: ")) # Ask user for a number
    
    if number != 0: # If the user enters 0, stop the loop
        total = total + number # Add the number to the total
        print(f"Current total: {total}") # Print the current total

print(f"Final total: {total}") # Print the final total after the loop ends
print("_" * 40)