names = ['John', 'Bob', 'Mosh', 'Sarah', 'Marry']

print(names)
print(names[-2:])  # from index 3 until the end - returns a new list
print(names[2:4])
print(names)  # original list not affected
names[0] = 'Jon'
print(names)
