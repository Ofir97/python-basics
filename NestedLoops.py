for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

print('-----------------------------')
numbers = [5, 2, 5, 2, 2]
for number in numbers:
    stars = ''
    for star in range(number):
        stars += 'X'
    print(stars)

print('-----------------------------')
for number in numbers:
    print('X' * number)
