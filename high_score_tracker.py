while True:
    
    user_input = input("Enter your game score (or type 'stop' to end): ")

    if user_input.strip().lower() == "stop":
        print("Game session ended!")
        break

    score = int(user_input)

    if score > 100:
        print("Wow! That's a new high score!")
    else:
        print("Good try, keep playing!")