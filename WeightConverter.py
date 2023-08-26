weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.lower() == 'l':
    print(f'You are {0.45 * weight} kgs')
elif unit.lower() == 'k':
    print(f'You are {2.20 * weight} pounds')
else:
    print('invalid weight unit')
