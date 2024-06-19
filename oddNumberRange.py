def sum_of_odd_numbers(limit):
    sum_odd = 0
    for num in range(1, limit + 1, 2):
        sum_odd += num
    return sum_odd
limit = 10
result = sum_of_odd_numbers(limit)
print(f"The sum of odd numbers up to {limit} is: {result}")
