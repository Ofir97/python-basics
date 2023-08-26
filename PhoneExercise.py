phone = input('Phone: ')
digits_mapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}
phone_number = ''
for digit in phone:
    phone_number += digits_mapping.get(digit, '!') + ' '

print(phone_number)