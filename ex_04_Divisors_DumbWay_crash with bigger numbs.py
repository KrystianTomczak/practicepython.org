num = int(input("Please choose a number to divide: "))
listRange = list(range(1,num+1))
divisorList = list()

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)