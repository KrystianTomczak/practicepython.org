import random

#compute random lists
list_a = [random.randint(0, 100) for num in range(0, 50)] #comprehension for number generator
list_b = [random.randint(0, 40) for num in range(0, 10)] #comprehension for number generator

#Using list comprehension
def common(a, b):
    new_list_1 = []
    [new_list_1.append(number) for number in list_a if number in list_b if number not in new_list_1]
    return new_list_1

#With set method:
def common_v2(a, b):
    set_a = set(list_a) #remove duplicates on the random lists a
    set_b = set(list_b) #remove duplicates on the random lists b
    new_list_2 = []
    for number in set_a:
        if number in set_b:
            new_list_2.append(number)
    return new_list_2

#Old method (ex_05)
def common_v3(a, b):
    new_list_3 = []
    for number in a:
        if number in b:
            if number not in new_list_3:
                new_list_3.append(number)
    return new_list_3

print("List a =", list_a)
print("List b =", list_b)
print("List comprehension method:", sorted(common(list_a, list_b)))
print("Set method:", sorted(common_v2(list_a, list_b)))
print("Old, loop method: ", sorted(common_v3(list_a, list_b)))
