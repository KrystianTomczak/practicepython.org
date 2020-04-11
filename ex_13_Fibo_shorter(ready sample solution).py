def Fibonacci():
    count = int(input("How many fibonumbers?"))
    fibo = [1, 1]
    while len(fibo) < count:
       fibo += [fibo[-1] + fibo[-2]]
    print(fibo[0:count])


Fibonacci()