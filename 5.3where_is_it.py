import random

numbers = [random.randint(1, 50) for _ in range(10)]

print("List:", numbers)

value = int(input("Value to find: "))

found = False

for index in range(len(numbers)):
    if numbers[index] == value:
        print(f"{value} is at index {index+1}.")
        found = True

if not found:
    print(f"{value} is not in the list.")