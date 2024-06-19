def is_palindrome(number):
    original_number = number
    reversed_number = 0
    
    while number > 0:
        remainder = number % 10
        reversed_number = reversed_number * 10 + remainder
        number = number // 10
    
    return original_number == reversed_number
number = 12321
result = is_palindrome(number)
if result:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
