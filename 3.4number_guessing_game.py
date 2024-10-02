import random
answer = random.randint(1,11)

print("I'm thinking of a number between 1-10")
guess = int(input("Please input your guess: "))

if guess == answer:
    print(f"That's right!  My secret number was {answer}!")
elif guess <=0 or guess >= 10:
    print("Please print a number that is within 1-10")
else:
    print(f"Sorry but I was thinking of the number {answer}")