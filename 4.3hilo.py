import random
print("I'm thinking of a number between 1-100, you have 7 tries")
number = random.randint(1,10)
counter = 1
while counter <= 7:
    guess = int(input("Please enter your first guess"))
    if guess < number:
        print("You are too low")
    elif guess > number:
        print("You are too high")
    elif guess == number:
        print("Wow, you got the number, good job!")
        break
    counter += 1
if counter > 7:
    print(f"Sorry, you didn't guess it in 7 tries. The number was {number}. You lose")