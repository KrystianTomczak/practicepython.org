import random

lst = [random.randint(1, 40) for num in range(0, 20)]
print(sorted(([num for num in lst if num % 2 == 0])))