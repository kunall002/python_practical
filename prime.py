def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
number = 29
result = is_prime(number)
if result:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
