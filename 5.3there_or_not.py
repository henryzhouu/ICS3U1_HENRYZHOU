import random
trueorfalse = False
numbers = []
for _ in range(10):
    numbers.append(random.randint(1, 50))

print("List:", numbers)

value = int(input("Value to find: "))

for num in numbers:
    if num == value:
        trueorfalse = True

if trueorfalse == True: 
    print(f"{value} is in the list")
else:
    print(f"{value} is not in the list")