a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lst = list()
for number in a:
    if number < 5:
        lst.append(number)
print(lst)

lst_sec = list()
numb = input("Number: ")
for number in a:
    if int(numb) > number:
        lst_sec.append(number)
print(lst_sec)

