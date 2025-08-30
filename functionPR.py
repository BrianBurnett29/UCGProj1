def welcome_message():
    print("=" * 30)
    print("Welcome to the Function PR module!")
    print("_" * 30)
    
def get_test_scores():
    first = float(input("Enter the first test score: "))
    second = float(input("Enter the second test score: "))
    third = float(input("Enter the third test score: "))
    return first, second, third

def calculate_average(first, second, third):
    average = (first + second + third) / 3
    return average  

def letter(average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:     
            return "C"
        elif average >= 60:
            return "D"   
        else:
            return "F"

def display_results(first, second, third, average, letter):
    print("\nYour Results:")
    print(f"Test Scores: {first}, {second}, {third}")
    print(f"Average Score: {average:.1f}")
    print(f"Letter Grade: {letter}")

def main():
    welcome_message()
    first, second, third = get_test_scores()
    average = calculate_average(first, second, third)
    letter_grade = letter(average)
    display_results(first, second, third, average, letter_grade)
    
    print("Thank you for using the Function PR module!")
    
    

if __name__ == "__main__":
    main()