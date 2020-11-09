def factorial(n):
    if n >= 0:
        if n == 0:
            return 1
        if n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    else:
        return 'Factorial of negative number is not possible'


print(factorial(75))
