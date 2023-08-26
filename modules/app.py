# import converters # able to access all functions in converters
from converters import kg_to_lbs  # import specific function from converters
from utils import find_max

print(kg_to_lbs(70))
numbers = [10, 3, 9, 11, 23, 100, -3]
print(find_max(numbers))
print(max(numbers))
