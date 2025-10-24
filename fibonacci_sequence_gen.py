print("---Fibonacci Sequence Generator---")
n = int(input("How many Fibonacci numbers would you like to generate? "))
a = 0
b = 1
for i in range(n):
    print(a, end=' ')
    a, b = b, a+b