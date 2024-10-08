import random
print("Here comes the dice")
dices_rolled = 0
while dices_rolled <= 4:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(f"Dice 1:{dice1}")
    print(f"Dice 2:{dice2}")
    print(f"The sum is {dice1+dice2}")
    dices_rolled += 1