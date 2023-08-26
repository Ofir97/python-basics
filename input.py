name = input('What is your name? ')
favorite_color = input('What is your fave color? ')
birth_year = input('Birth year: ')
print(type(birth_year))

age = 2023 - int(birth_year)
print(type(age))
print(name + ' likes ' + favorite_color)
print('Your age is: ' + str(age))

# ---------------------------------------------------- #

weight_lbs = input('What is your weight (lbs)? ')
weight_kg = 0.45 * int(weight_lbs)
print('Your weight is ' + str(weight_kg))

