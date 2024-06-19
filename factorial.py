def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

num = int(input("Enter a number: "))
print("Factorial (Iterative):", factorial_iterative(num))
print("Factorial (Recursive):", factorial_recursive(num))
