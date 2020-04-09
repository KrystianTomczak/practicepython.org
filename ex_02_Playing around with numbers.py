numb = input("Please enter number: ")
check = input("Please enter second number: ")
calc = int(numb) % int(check)
if int(numb) % 4 == 0:
    print("Is multiplied by 4")
elif int(numb) % 2 == 0:
    print("Even")
else:
    print("Odd")

if calc == 0:
    print("divides evenly")
else:
    print("Not evenly")
