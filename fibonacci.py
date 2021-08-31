# Python 3: Fibonacci series up to n
def fib():
    n=int(input("write a number:"))
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib()
def buy():
    print("Thank you for using  my code")
buy()