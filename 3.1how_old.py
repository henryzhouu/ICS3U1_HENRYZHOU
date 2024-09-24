name = input("What is your name?    ")
age = int(input(f"OK, {name}, how old are you?  "))
print()
if age <16:
    print("You can't drive {}".format(name))
if age < 18:
    print("You can't vote " + str(name))
if age < 21:
    print("You can't drink {}".format(name))
if age >= 21:
    print(f"You can do anything that is legal {name}" )

#Test Cases
#Inputs:  Processing:               Output:
#15         age<16 age<18 age<21     "You can't drive, You can't vote, You can't drink"
#17         age<18 age<21            "You can't vote, You can't drink"
#20         age<21                   "You can't drink"
#21         age >= 21                “You can do anything that’s legal.”
#26         age >= 21                “You can do anything that’s legal.”