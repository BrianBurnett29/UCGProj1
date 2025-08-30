import random

print("\n⁇ Welcome to the Guess the Number Game! 📖")

def guess_the_number():
    number_to_guess = random.randint(1, 10)  # Random number between 1 and 10
    attempts = 0 # Makes attempts counter
    guessed_correctly = False # Keeps track of whether the user has guessed correctly

    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        except ValueError:
            print("Please enter a valid integer.")
guess_the_number()