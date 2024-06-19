my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print(my_list)

removed_element = my_list.pop()
print(removed_element)
print(my_list)

index_of_3 = my_list.index(3)
print(index_of_3)

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

keys = my_dict.keys()
print(keys)

values = my_dict.values()
print(values)

age = my_dict.get('age')
print(age)
