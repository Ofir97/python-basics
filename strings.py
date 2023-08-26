course1 = "Python's Course for Beginners"
course2 = 'Python for "Beginners"'
print(course1)
print(course2)
print(course1[0])
print(course1[-1])  # return last char index
print(course1[0:3])  # return chars from 0 to 3 (exclude)
print(course1[0:])  # return all chars
print(course1[1:])  # return all chars from index 1
print(course1[:5])  # return all chars from index 0 to 5 (exclude)
print(course1[:])  # return all chars
another = course1[:]  # another variable is a copy of course1

message = '''
Hi John,

Here is our first email to you.

Thank you,
The support team

'''
print(message)
print(another)
print('Jennifer'[1:-1])
