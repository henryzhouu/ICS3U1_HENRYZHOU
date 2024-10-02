#1) when we change randrange from 1-6 to 1-5 it changes the range from(1-5) to (1-4)
#2) When we put in the seed function and put in an integer like 400, it makes the random values consistent
#3) Those random numbers are changed into something else, but they stay consistent when printed
#4) A game I know that uses seeds is minecraft. The seeds help generate same worlds.
import random
random.seed(200)


x = random.randrange(10)  # 0-9
print(f"My random number is {x}.")

print()
print("Here are some random numbers from 1 to 5...")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6), end=", ")
print(random.randrange(1, 6))

print()
print("Here are some random numbers from 1 to 100...")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101), end=", ")
print(random.randrange(1, 101))

print()
print("Will these next two random number be the same?")
a = random.randrange(10)  # 0-9
b = random.randrange(10)

if a == b:
    print(f"Wow! Both numbers were {a}!")
else:
    print("The two random numbers were different. Not too surprising.")