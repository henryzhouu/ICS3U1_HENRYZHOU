import random

while True:
    flip = random.randrange(2)  # 0-1

    if flip == 1:
        coin = "HEADS"
    else:
        coin = "TAILS"

    print("You flip a coin and it is... " + coin)

    again = input("Would you like to flip again (y/n)? ")
    if again != "y":
        break

# The code as given does not run. Notice that the while tests if again == "y", but the variable again doesn’t have a string value at first. Give it a string value so that the code will not encounter a run-time error and the loop will run at least once.
# done
# # Now that program is working, change the loop from a pre-test while loop to a post-test “while-true” loop. Make sure it still works.
# done
# What happens if you delete the again = "y" line right before the loop? Does the program still work? Why or why not? (Answer in a comment.)
# Program still works but when you ask the end the code it doesn't work.
