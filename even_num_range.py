def sum_of_even_numbers(limit):
    sum_even = 0
    for num in range(2, limit + 1, 2):
        sum_even += num
    return sum_even
limit = 10
result = sum_of_even_numbers(limit)
print(f"The sum of even numbers up to {limit} is: {result}")
