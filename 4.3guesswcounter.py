import random
answer = random.randint(1,11)
counter = 1
print("I'm thinking of a number between 1-10")
guess = int(input("Please input your guess: "))

while guess != answer:
    print("That's wrong")
    print("Keep guessing")
    guess = int(input("Please input your guess: "))
    counter += 1

print(f"Good job, you got the right number, it only took you {counter}, tries!")