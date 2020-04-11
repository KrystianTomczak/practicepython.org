#Exerciese 15 - Reverse word order
user_input = input("User input: ")

def backwards():
    lst = user_input.split()
    lst_back = lst[::-1]
    print(" ".join(lst_back))

backwards()

