# Fibonacci

def Fibonacci():
    numbs = int(input("Please enter how many numbers would You like to generate: "))
    numb = 1
    if numbs == 0:
        fib = []
    elif numbs == 1:
        fib = [1]
    elif numbs == 2:
        fib = [1, 1]
    elif numbs > 2:
        fib = [1, 1]
        while numb < (numbs-1):
            fib.append(fib[numb] + fib [numb - 1])
            numb += 1
    return fib

print(Fibonacci())



