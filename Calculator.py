sum = 0

while True:
    userInput = input("Enter the price and press q to quit: \n")
    if (userInput != 'q'):
        sum += int(userInput)
        print(f"Order total so far:  {sum}")
    else:
        print(f"Your total bill is {sum}.")
        print("Thank you for shopping with us.")
        break