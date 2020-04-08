import random

def game():
    user_pick = input("Choose rock, paper or scissors?")  # User pick
    print("You picked: " + user_pick)
    item = ["rock", "paper", "scissors"]    # Auto pick
    auto_pick = random.choice(item)
    print("Computer picked: " + auto_pick)
    if user_pick == auto_pick:
            return("Result: draw!")
    elif user_pick == "paper":
        if auto_pick == "rock":
            return ("Result: you won!")
        else:
            return ("Result: you lost...")
    elif user_pick == "rock":
        if auto_pick == "scissors":
            return ("Result: you won!")
        else:
            return ("Result: you lost...")
    elif user_pick == "scissors":
        if auto_pick == "paper":
            return ("Result: you won!")
        else:
            return ("Result: you lost...")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")

def restart():
    while True:
        while True:
            answer = input("Run again?")
            if answer in ("y", "Yes", "yes", "No", "no", "n", ""):
                break
            print("Invalid input. Type 'yes' or 'no'")
        if answer == "y" or answer == "yes" or answer == "Yes" or answer == "":
            print(game())
        else:
            print("Bye bye. Please rate us! See You soon.")
            break

def main():
    user = input("Can You tell me your name?")
    if len(user) >= 1:
        enter = input(("Hello " + user + " let's play rock, paper, scissors. Ready? Press Enter to start."))
        if enter == "":
            print(game())
            restart()
    else:
        print("Something went wrong. Please try again.")
        restart()

main()
