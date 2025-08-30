#Example 1 Basic For Loop
print("\nExample 1: Basic For Loop")
print("-" * 30)
for i in range(5):
    print(f"This is loop number {i}")
print("Loop is finsihed!\n")

#Example 2 Counting from 1 to 10
print("\nExample 2: Counting from 1 to 10")
print("-" * 30)
for number in range(1, 11):
    print(f"Count: {number}")
print("Counting complete!\n")

#Example 3 List Looping
print ("\nExample 3: Looping through a list")
print("-" * 30)
movies = ["Better Man", "Avengers", "42", "Batman", "Deadpool 2"]
for movie in movies:
    print(f"Movies: {movie}!")   
print("All movies listed!\n")

#Example 4 Skip Counting (STEP)
print("\nExample 4: Skip Counting")
print("-" * 30)
for num in range(0, 21, 2):
    print(f"Even number: {num}")
print("All even numbers from 0 to 20!\n")

#Example 5 Multiplication Table
print("\nExample 5: Multiplication Table")
print("-" * 30)
for i in range (1, 11):
    result = 5*i
    print(f"5 x {i} = {result}")
print("Multiplication table for 5 completed!\n")

#Example 6 Looping through letters
print("\nExample 6: Looping through letters")
print("-" * 30)
word = "Python"
for letter in word:
    print(f"Letter: {letter}")
print(f"The word '{word}' has {len(word)} letters!\n")

#Example 7 Nested Loops
print("\nExample 7: Nested Loops")
print("-" * 30)
for row in range(3): # Outer loop - runs 3 times
    print(f"Row {row + 1}: ", end="") # end="" keeps on the same line
    for star in range(5): # Inner loop - runs 5 times for each row
        print("* ", end="") # Print stars in the same line
print("patterned output completed!\n")

#Ask user how many times to say hello
times = int(input("How many times do you want to say hello? "))
for i in range(times):
    print(f"Hello! #{i + 1}")
print("All done saying hello!\n)")