#hard version help with setting the min
from random import randint

secret_number = int(input("secret number between 1 and 100?"))
computer = randint(0, 100)
ranmax = 100
ranmin = 0
print(computer)
loser = True
for _ in range(1, 10):

    if secret_number < computer:
        print(computer)
        print("Computer, you are too high")
        print("Num of tries: " + str(_))
        ranmax = computer
        computer = randint(ranmin, computer)
        loser = True
    elif secret_number > computer:
        print(computer)
        print("The guess is too low")
        print("Num of tries: " + str(_))
        ranmin = computer + 1
        computer = randint(computer, ranmax)
        loser = True
    elif secret_number == computer:
        print(computer)
        print("Spot on")
        print("Num of tries: " + str(_))
        loser = False
        break

print("Game over")
if loser:
    print("You are a dumb computer.")