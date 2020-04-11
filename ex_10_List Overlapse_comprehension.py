import random

#computing random lists
list_a = random.sample(range(50), 30)
list_b = random.sample(range(40), 10)
new_list = [] #for list comprehension w/o using set method

#For checking purposes only
print(list_a)
print(list_b)

#List comprehension
[new_list.append(num) for num in list_a if num in list_b if num not in new_list]
print(sorted(new_list))

#List comprehension with set method - even better only 4 lines (incl. import for computing random list)
print(sorted([num for num in set(list_a) if num in list_b]))




