#IMPORT REGULAR EXPRESSIONS (REGEX) & STRING STATEMENTS


import re
import string

def main():
    

    #Introduce the game
    print("The Drive to a Lost Home")
    
    print("A story game made by Brian, Jeremiah, Preston")

    #Introducing and naming player and partner
    player_name = input("What is your player name ")

    side_character_pick = input("Who do you want to assist you in your journey? (Jeremiah, Brian, Preston) ")
   
    if side_character_pick == "Jeremiah": 
            print("Jeremiah will join you on your journey. ")
    
    elif side_character_pick == "Brian":
            print("Brian will join you on your journey. ")
    
    elif side_character_pick == "Preston":
            print("Preston will join you on your journey. ")
    
    else:
           print("Come on man pick one of the 3 options") 
   
    input(f"{player_name} and {side_character_pick} are driving to Nevada for the Summer.\nAs they drive the car runs out of gas (Press Enter)").lower()

    print("  ______       ")
    print(" /|_||_\ '.__  ")
    print("(.            }")
    print("-( ) - - (  )- ")

    user_action = input(f"{side_character_pick}: What are we gonna do we're stuck next to the woods {player_name}?\n{side_character_pick}: what do you want to do {player_name}? ")
    
    #Clean User input
    user_action_clean = user_action.lower().translate(str.maketrans('', '', string.punctuation))
    
    keywords = ["stay", "gas", "walk(?:ing)?", "woods"]
    
    # Build regex pattern for whole word matching
    pattern = r'\b(' + '|'.join(keywords) + r')\b'

    # Search for keywords in user input, case-insensitive
    match = re.search(pattern, user_action_clean, re.IGNORECASE)

    if match:
        found_word = match.group(0).lower()  # normalize to lowercase for consistent responses
        
        if found_word == "stay":
            print(f"{side_character_pick} nods. 'Alright, we'll stay here and wait for help.'")
            
        elif found_word == "gas":
            print("You realize the car is out of gas. You need to find some soon. ")
            
        elif found_word in ["walk", "walking"]:
            print(f"{player_name} suggests walking to find help. {side_character_pick} agrees cautiously. ")
            
        elif found_word == "woods":
            print(f"You look towards the woods nearby. It's dense but might hold some answers.")
            
    else:
        print("Hmm, I didn't understand that. Try to decide whether to stay, look for gas, walk, or check the woods.")

main()
