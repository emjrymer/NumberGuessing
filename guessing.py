#first try with help from other student
rando = 10

while True:
    user_input = input("Guess a number: ")

    if user_input.isalpha():
        print("I said, enter a number, dummy: ")

    elif int(user_input) > rando:
        print(user_input)
        print("Too high")

    elif int(user_input) < rando:
        print("Too low")

    elif int(user_input) == rando:
        print("Correct!  You guessed: " + str(user_input))
        break