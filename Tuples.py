numbers = (1, 2, 3)  # immutable list, only count(), index() methods -> only get info, not change
print(numbers[0])
print(numbers[1])
print(numbers[2])

print('----- unpacking -----')

coordinates_tuples = (1, 2, 3)
x, y, z = coordinates_tuples
print(f'x={x}, y={y}, z={z}')

coordinates_list = [1, 2, 3]
x, y, z = coordinates_list
print(f'x={x}, y={y}, z={z}')
