def greet_user(first_name, last_name):  # function: parameters
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


print('Start')
greet_user('John', 'Smith')  # function invoke: positional arguments (order matters)
greet_user(last_name='Lue', first_name='Marry')  # function invoke: key-word argument (position does not matter)
# improves readability especially for numeric arguments

print('Finish')
