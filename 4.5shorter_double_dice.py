import random
print("Here comes the dice!")

while True:
    a = (random.randint(1,6))
    b = (random.randint(1,6))
    print(f"roll 1:{a}")
    print(f"roll 2:{b}")
    print(f"The total is {a+b}!")
    if a == b:
        break
