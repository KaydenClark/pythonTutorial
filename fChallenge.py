#goal is to print and F using x's

numbers = [5, 2, 5, 2, 2]

for i in numbers:
    row = ''
    for j in range(i):
        row += 'x'
    print(row)