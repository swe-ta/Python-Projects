import random

def swg():
    Round = 1
    user_point = 0
    comp_point = 0

    while Round <= 3:
        print(f"\nRound {Round}")
        user = input("Choose between Snake/Water/Gun: ").casefold()
        computer = random.choice(["Snake", "Water", "Gun"]).casefold()
        print(f"Computer chose: {computer}")

        if user == computer:
            print("Match is draw!")

        elif user == "snake" and computer == "water":
            print("You win.")
            user_point += 1

        elif user == "water" and computer == "snake":
            print("You lose!")
            comp_point += 1

        elif user == "gun" and computer == "snake":
            print("You win.")
            user_point += 1

        elif user == "snake" and computer == "gun":
            print("You lose!")
            comp_point += 1

        elif user == "water" and computer == "gun":
            print("You win.")
            user_point += 1

        elif user == "gun" and computer == "water":
            print("You lose!")
            comp_point += 1

        else:
            print("Invalid input. Please choose Snake, Water, or Gun.")
            continue

        Round += 1
    print("\nFinal Results:")
    print(f"Your points: {user_point}")
    print(f"Computer points: {comp_point}")

    if user_point > comp_point:
        print(" Congrats! You win this game.")
    elif user_point < comp_point:
        print("😢 You lose this game.")
    else:
        print("😐 The game is a draw.")

while True:
    print("\n1. Start the game")
    print("2. Exit the game")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        swg()
    elif choice == 2:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")
