import random
print("I have chosen a number between 1 and 10.  Try to guess it.")
x = random.randrange(1, 10)
counter = 1
while True:
    counter += 1
    guess = int(input("Your guess: "))
    if guess == x:
        print(f"That's right \nWow you guessed it in {counter} tries")
        break
    else:
        print("Keep guessing")