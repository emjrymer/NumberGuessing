#hardest version
from random import randint

ranmax = 100000
ranmin = 0
counter = 0

secret_number = int(input("Give the computer a Secret Number to guess between " + str(ranmin) + " and " + str(ranmax) +": "))
computer = randint(ranmin, ranmax)

loser = True

while loser:

    if secret_number < computer:
        print(computer)
        print("Computer, you are too high")
        counter = counter + 1
        print("Number of tries: " + str(counter))
        ranmax = computer
        computer = (ranmax - ((ranmax - ranmin) //2))
        loser = True

    elif secret_number > computer:
        print(computer)
        print("The guess is too low")
        counter = counter + 1
        print("Number of tries: " + str(counter))
        ranmin = computer
        computer = (((ranmax - ranmin) //2) + ranmin)
        loser = True

    elif secret_number == computer:
        print(computer)
        print("Spot on!!")
        counter = counter + 1
        print("Number of tries: " + str(counter))
        loser = False

print("Game over :'(")

if loser:
    print("You are a dumb computer. >:(")