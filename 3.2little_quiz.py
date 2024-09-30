input("Are you ready for a little quiz? ")
print("Okay! Here it comes!")
score = 0

ans1 = float(input("\n What is 30 x 113: "))
if ans1 == 30*113:
    print("\n   Great Job!")
    score += 1
else:
    print("That's Wrong :(")
ans2 = str(input("\n What is my name: "))
if ans2 == "Henry":
    print("\n   Great Job!")
    score += 1
else:
    print("That's Wrong :(")
ans3 = input("When is my birthday? ")
if ans3 == "February 25":
    print("\n   Great Job!")
    score += 1
else:
    print("That's Wrong :(")

print(f"Your score is {score}")