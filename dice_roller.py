import random
def roll_dice():
    # Generate a random number between 1 and 6
    dice_result = random.randint(1, 6)
    print(f"You rolled a {dice_result}")
# Main program
print("Welcome to the Dice Roller!")
while True:
    roll_dice()  # Roll the dice
    roll_again = input("Do you want to roll again? (yes/no): ").strip().lower()
    if roll_again != "yes":
        break  # Exit the loop if the user doesn't want to roll again
print("Thanks for playing!")