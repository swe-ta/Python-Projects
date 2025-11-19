name = input(str("Type you name: ")).casefold()
print("Welcome,",name,"to this adventure!")

answer = input ("You are one a dirt road, it has come to an end and you can go left and right. Which way you like to go?").casefold()

if answer == "left":
    answer = input(str(
        "You come to a river, you can walk around it  swim acros. Type walk to walk and swim to swim across: ")).casefold()

    if answer == "swim":
         print("You swam across and eaten by an aligator.")

    elif answer == "walk":
         print("You walked many miles, ran out of water and you lost the game.")

    else:
          print("Not a valid option.You lose!")

elif answer == "right":
    answer = input(str(
        "You come to a bridge, it looks lovely, do you want to to cross it or head back(cross/back)? ")).casefold()
    if answer == "back":
        print("You go back and loose!")

    elif answer == "cross":
        answer = input("YOu cross the bridge and meet a stranger. Do you want to talk(yes/no)?").casefold()

        if answer == 'yes':
            print("You talk to the stranger. YOu win!")
        elif answer == 'no':
            print("You ignore the stranger. You loose!")

        else:
            print("Not a valid option.You lose!")

    else:
        print("Not a valid option.You lose!")
else:
    print("Not a valid option.You lose!")

print("Thank you for trying," ,name)

