getal = int(input("Van welke getaal wil je de faculteit weten?" ))
# Factorial
# !4 = !3 * 4
#
# factorial(0) = 1
# factorial(n) = n * factorial(n-1)
# def factorial(n):         if we would like to use function
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
factorial = 1
for n in range(1, getal + 1): # loop from 1 till n
    factorial = factorial * n
print(factorial)
