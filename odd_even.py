def find_odd_even_numbers(limit):
    odd_numbers = []
    even_numbers = []
    
    for i in range(1, limit + 1):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)
    
    print(f"Odd numbers up to {limit}: {odd_numbers}")
    print(f"Even numbers up to {limit}: {even_numbers}")
limit = 20
find_odd_even_numbers(limit)
