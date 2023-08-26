course = 'Python for Beginners'
print(len(course))  # string length - count num of chars in string : function
print(course.upper())  # string method: not modifying string, only clone and modify
print(course.lower())
print(course)
print(course.find('P'))  # index of first occurrence of character: case-sensitive
print(course.find('Beginners'))  # index of first occurrence of word Beginners: index [11]
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))
print('Python' in course)  # returns true if 'Python' exists in string, otherwise false
print('python' in course)  # returns true if 'Python' exists in string, otherwise false

