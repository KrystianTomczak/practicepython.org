import random

def game_number():
    number = random.randint(1, 20) #return random number from indicated range
    #print(number) for testing purposes only
    guess = 0  # User guess
    count = 0  # Counter of shots
    while True:
        count += 1
        try:
            guess = (int(input("Guess the number: ")))
        # print(type(guess))
        except:
            print("Invalid input, please enter numbers. You lost one chance. Please guess again.")
            continue
        if guess == number:
            if count <= 1:
                print("Impressive! You guessed the lucky number. You tried only " + str(count) + " time.")
            elif count >= 2 and count <= 4:
                print("Good! You guessed the lucky number. You tried " + str(count) + " times.")
            elif count == 5:
                print("Uff! That was close. It was You last chance. You managed in " + str(count) + " times.")
            break
        if count >= 5:
            print("Missed! You wasted five shots. The lucky number was: " + str(number) + ". Please try again!")
            break
        elif guess > number:
            print("Too high. Try again")
        elif guess < number:
            print("Too low. Try again")

def restart():
    while True:
        while True:
            answer = input("Run again? (y/n): ")
            if answer in ("y", "Yes", "yes", "No", "no", "n"):
                break
            print('Invalid input.')
        if answer == "y" or answer == "yes" or answer == "Yes" or answer == "":
            game_number()
        else:
            print("Bye bye. Please rate us! See You soon.")
            break

def main():
    user = input("Can You tell me your name?")
    if len(user) >= 1:
        enter = input(("Hello " + user + " let's play guessing game. You have five shots. Give me Your lucky number from 1 to 20. Press ENTER to begin."))
        if enter == "":
            game_number()
            restart()
    else:
        print("Noob. Let's go directly to the game")
        game_number()
        restart()

main()