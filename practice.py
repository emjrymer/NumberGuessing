#second try with help
rando = 4
loser = False
for _ in range(1,6):

    guess = int(input("Guess a number: "))

    if guess > rando:
        print("Your number is too high")
        print("Number of tries: " + str(_))
        print("Close, only " + str(guess - rando) + " off.")
        loser = True
    elif guess < rando:
        print("Your number is too low")
        print("Number of tries: " + str(_))
        print("Close, only " + str(rando - guess) + " off.")
        loser = True
    elif guess == rando:
        print("Congrats, you did it!")
        print("Number of tries: " + str(_))
        loser = False
        break
if loser:
    print("Better luck next time.  You ran out of guesses.")
