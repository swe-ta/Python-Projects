print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").casefold()
if playing != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What does CPU stand for? ").casefold()
if answer == "Central Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").casefold()
if answer == "Graphics Processing Unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").casefold()
if answer == "Random Access Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? ").casefold()
if answer == "Read Only Memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")

