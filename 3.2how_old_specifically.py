name = input("What is your name (Sorry I keep forgetting): ")
age = int(input(f"Okay, {name}, how old are you? "))

if age < 16:
    print(f"You can drive, {name}.")
elif 16  <= age <= 17:
    print(f"You can drive but not vote, {name}.")
elif 18 <= age <= 20:
    print(f"You can vote but not rent a car, {name}.")
else:
    print(f"You can pretty much do anything, {name}")