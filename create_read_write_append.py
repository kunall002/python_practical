with open('example.txt', 'w') as file:
    file.write('This is the first line.\n')
    file.write('This is the second line.\n')

with open('example.txt', 'r') as file:
    content = file.read()
    print("File content after initial write:")
    print(content)

with open('example.txt', 'a') as file:
    file.write('This is an appended line.\n')

with open('example.txt', 'r') as file:
    content = file.read()
    print("File content after appending:")
    print(content)
