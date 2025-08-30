weather = input("Is it raining?🌧️ (yes/no) ")
if weather == "yes" or weather == "Yes":
    umbrella = input(f"Oh {weather} take an umbrella. Are you planning on going somewhere?☔️ (Yes/No) ")
    if umbrella == "yes" or umbrella == "Yes":
        going = input(f"{umbrella}, okay stay dry and safe! Where are you going? 🌂 ")
        if going == "home" or going == "Home":
            print(f"Oh {going}? I hope you have a good time at home. 🏠 ")
        elif going == "work" or going == "Work":
            print(f"Oh {going}? I hope you have a good day at work. 💼 ")
        elif going == "school" or going == "School":
            print(f"Oh {going}? I hope you have a good day at school. 🎓 ")
        elif going == "store" or going == "Store":
            print(f"Oh {going}? I hope you find what you need at the store. 🏪 ")
        elif going == "park" or going == "Park":
            print(f"Oh {going}? I hope you have a good time at the park. 🌳 ")
        elif going == "gym" or going == "Gym":
            print(f"Oh {going}? I hope you have a good workout at the gym. 🏋️ ")
        elif going == "restaurant" or going == "Restaurant":
            print(f"Oh {going}? I hope you enjoy your meal at the restaurant. 🍽️ ")
        else:
            print("You lost me there, I don't know what to say. 🤷 ")    
    elif umbrella == "no" or umbrella == "No":
        input(f"{umbrella}? Oh okay I assume you're going to stay where you are then. 🌏 ")  
    else:
        print("AWHHHHHHHHHHHHHHHHHH! I don't know what to do with that answer. 🤷 ")
elif weather == "no" or weather == "No":
    age = int(input(f"Oh {weather}? Time to have fun. How old are you?☀️ "))
    if age < 18:
        print(f"Oh {age}? You are still young and have a lot to learn. 🌱 ")
    elif age >= 18 and age < 30:
        print(f"Oh {age}? You are in your prime years, enjoy them! 🌟 ")
    elif age >= 30 and age < 50:
        print(f"Oh {age}? You are in the middle of your life, make the most of it! 🌈 ")
    elif age > 50 and age < 100:
        print(f"Oh {age}? You are wise and experienced, share your knowledge! 📚 ")
    else:
        print("Oh you're one of those. 😒")
else:
    input("Oh umm good? Is it good? Are you good? Press enter real quick. 🧐")
    name = input("Thank you for using the weather app! What is your name? 🌤️")
    input(f"Are you supposed to be here {name}? Nobody has ever been here before. 🤔")
    input(f"I guess you can stay {name}, but I don't know what to do with you. 🤷")
    input("Press enter to exit the app. 👋")