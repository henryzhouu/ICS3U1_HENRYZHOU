import random

numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 50))

print("List:", numbers)

value = int(input("Value to find: "))

count = 0
for num in numbers:
    if num == value:
        count += 1

print(f"{value} was found {count} time(s).")