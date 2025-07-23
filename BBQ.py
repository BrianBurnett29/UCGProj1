#Function to trigger the start of the game so we can end it at the proper time
def run_trivia_game():
   
   #asks the question and the answers are seperated with brackets

    questions = [
        {"question": "What is the initial release year of roblox?", "options": ["2010", "2003", "2006"], "answer": "2006"},
        {"question": "Kendrick Lamar released his album Section.80 on July 2nd, 2011. What was the third song on the album?", "options": ["ADHD", "King Kunta", "YAH"], "answer": "ADHD"},
        {"question": "Who is the 20th President?", "options": ["Abraham Lincoln", "James Garfield", "William Mckinley"], "answer": "James Garfield"},
        {"question": "When was the first cheese wheel made?", "options": ["7,000 B.C.", "600 AD", "1755"], "answer": "7,000 B.C."},
        {"question": "Why is honey never spoiled?", "options": ["It's too lazy", "Too sweet to die", "Honey does expire"], "answer": "Too sweet to die"},
    ]

    score = 0

#Introduces the game, gives the user a prompt to press Enter in order to continue
    print("\n🤮_______BJJ's_Trivia_Wivia________🥶")
    print("By Brian, Jeremiah, and Jeremy\n")
    input("Press Enter to begin...")

    for q_data in questions:
        print(f"\n{q_data['question']}")
        for i, option in enumerate(q_data['options']):
            print(f"{i+1}. {option}")

        user_answer = input("Enter the number of your answer: ")

        try:
            chosen_index = int(user_answer) - 1
            if 0 <= chosen_index < len(q_data['options']) and q_data['options'][chosen_index] == q_data['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was: {q_data['answer']}")
        except ValueError:
            print("Invalid input. Please enter a number.")
            print(f"The correct answer was: {q_data['answer']}")
            
    print(f"\nGame Over! You scored {score} out of {len(questions)}.")

if __name__ == "__main__":
    run_trivia_game()