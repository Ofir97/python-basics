from pathlib import Path

path = Path("emails")
# print(path.mkdir())
print(path.absolute())

current_path = Path()
print(current_path.absolute())
files = current_path.glob('*.py')  # all py files in current path
for file in files:
    print(file)

print('--------------------------------')

for item in current_path.glob('*'):  # all files/dirs in current path
    print(item)
