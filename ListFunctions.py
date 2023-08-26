numbers = [5, 2, 8, 1, 9]
numbers.append(20)
numbers.insert(0, 10)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
print(f'is 1 exist in list? {1 in numbers}')
print(f'index of first occurrence of number 8: {numbers.index(8)}')
numbers.clear()
print(numbers)
print(f'is 1 exist in list? {1 in numbers}')

new_list = [1, 2, 3, 3, 3, 1, 9, -3]
print(new_list.count(3))
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)

new_list2 = new_list.copy()
new_list.append(100)

print(new_list2)